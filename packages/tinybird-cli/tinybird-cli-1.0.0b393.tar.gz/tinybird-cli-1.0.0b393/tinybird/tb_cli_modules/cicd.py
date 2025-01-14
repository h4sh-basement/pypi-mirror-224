from enum import Enum
from pathlib import Path
from typing import Optional, Any, Dict, Union, Type, List
from os import getcwd
from string import Template
from dataclasses import dataclass

import click

from tinybird.client import TinyB
from tinybird.feedback_manager import FeedbackManager


class Provider(Enum):
    GitHub = 0
    GitLab = 1


GITHUB_CI_YML = """
    ##################################################
    ###   Visit https://github.com/tinybirdco/ci   ###
    ###   for more details or custom CI/CD         ###
    ##################################################

    name: Tinybird - CI Workflow

    on:
      workflow_dispatch:
      pull_request:
        branches:
         - main
         - master
        types: [opened, reopened, labeled, unlabeled, synchronize]

    concurrency: ${{ github.workflow }}-${{ github.event.pull_request.number }}

    jobs:
        ci: # ci using environments from workspace '$workspace_name'
          uses: tinybirdco/ci/.github/workflows/ci.yml@v1.1.2
          with:
            data_project_dir: .
          secrets:
            admin_token: ${{ secrets.ADMIN_TOKEN }}  # set admin token associated to an account in GitHub secrets
            tb_host: $tb_host
"""

GITHUB_CD_YML = """
    ##################################################
    ###   Visit https://github.com/tinybirdco/ci   ###
    ###   for more details or custom CI/CD         ###
    ##################################################

    name: Tinybird - CD Workflow

    on:
      workflow_dispatch:
      push:
        branches:
          - main
          - master
    jobs:
      cd:  # deploy changes to workspace '$workspace_name'
        uses: tinybirdco/ci/.github/workflows/cd.yml@v1.1.2
        with:
          tb_deploy: false
          data_project_dir: .
        secrets:
          admin_token: ${{ secrets.ADMIN_TOKEN }}  # set admin token associated to an account in GitHub secrets
          tb_host: $tb_host
"""


GITLAB_YML = """
    ##################################################
    ###   Visit https://github.com/tinybirdco/ci   ###
    ###   for more details or custom CI/CD         ###
    ##################################################

    include: "https://raw.githubusercontent.com/tinybirdco/ci/v1.1.2/.gitlab/ci_cd.yaml"

    .ci_config_rules:
      - &ci_config_rule
        if: $CI_PIPELINE_SOURCE == "merge_request_event"
      - &ci_cleanup_rule
        if: $CI_PIPELINE_SOURCE == "merge_request_event"

    .cd_config_rules:
      - &cd_config_rule
        if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

    .cicd_variables:
      variables: &cicd_variables
        TB_HOST: "$tb_host"
        ADMIN_TOKEN: $ADMIN_TOKEN  # set admin token associated to an account in GitLab CI/CD Variables
        DATA_PROJECT_DIR: "."
        TB_DEPLOY: "false"

    run_ci:  # ci using environments from workspace '$workspace_name'
      extends: .run_ci
      rules:
        - *ci_config_rule
      variables:
        <<: *cicd_variables

    cleanup_ci_env:
      extends: .cleanup_ci_branch
      needs: ["run_ci"]
      rules:
        - *ci_cleanup_rule
      variables:
        <<: *cicd_variables

    run_cd:  # deploy changes to workspace '$workspace_name'
      extends: .run_cd
      rules:
        - *cd_config_rule
      variables:
        <<: *cicd_variables

    cleanup_cd_env:
      extends: .cleanup_cd_branch
      needs: ["run_cd"]
      rules:
        - *cd_config_rule
      variables:
        <<: *cicd_variables
"""


@dataclass
class CICDFile:
    template: str
    file_name: str
    dir_path: Optional[str] = None
    warning_message: Optional[str] = None


class CICDGeneratorBase:
    cicd_files: List[CICDFile] = []

    def __call__(self, path: str, params: Dict[str, Any]):
        for cicd_file in self.cicd_files:
            if cicd_file.dir_path:
                Path(f'{path}/{cicd_file.dir_path}').mkdir(parents=True, exist_ok=True)
            file_path = f'{cicd_file.dir_path}/{cicd_file.file_name}' if cicd_file.dir_path else cicd_file.file_name
            content = Template(cicd_file.template).safe_substitute(**params)
            with open(f'{path}/{file_path}', 'w') as f:
                f.write(content)
            click.echo(FeedbackManager.info_cicd_file_generated(file_path=file_path))
            if cicd_file.warning_message is not None:
                return FeedbackManager.warning_for_cicd_file(file_name=cicd_file.file_name, warning_message=cicd_file.warning_message.format(**params))

    @classmethod
    def build_generator(cls, provider: str) -> Union['GitHubCICDGenerator', 'GitLabCICDGenerator']:
        builder: Dict[str, Union[Type[GitHubCICDGenerator],
                                 Type[GitLabCICDGenerator]]] = {Provider.GitHub.name: GitHubCICDGenerator,
                                                                Provider.GitLab.name: GitLabCICDGenerator}
        return builder[provider]()


class GitHubCICDGenerator(CICDGeneratorBase):
    cicd_files = [CICDFile(template=GITHUB_CI_YML,
                           file_name='tinybird_ci.yml',
                           dir_path='.github/workflows'),
                  CICDFile(template=GITHUB_CD_YML,
                           file_name='tinybird_cd.yml',
                           dir_path='.github/workflows',
                           warning_message='Set ADMIN_TOKEN in GitHub secrets. Copy from the admin token associated with your user account from {tokens_url}')]


class GitLabCICDGenerator(CICDGeneratorBase):
    cicd_files = [CICDFile(template=GITLAB_YML,
                           file_name='.gitlab-ci.yml',
                           warning_message='Set ADMIN_TOKEN in GitLab CI/CD Variables. Copy from the admin token associated with your user account from {tokens_url}')]


def ask_provider_interactively():
    provider_index = -1
    while provider_index == -1:
        click.echo(FeedbackManager.info_available_git_providers())
        for index, provider in enumerate(Provider):
            click.echo(f"   [{index + 1}] {provider.name}")
        click.echo("   [0] Cancel")

        provider_index = click.prompt("\nUse provider", default=1)

        if provider_index == 0:
            click.echo(FeedbackManager.info_cicd_generation_cancelled_by_user())
            return None

        try:
            return Provider(provider_index - 1).name
        except Exception:
            available_options = ', '.join(map(str, range(1, len(Provider) + 1)))
            click.echo(FeedbackManager.error_git_provider_index(host_index=provider_index, available_options=available_options))
            provider_index = -1


async def init_cicd(client: TinyB, workspace: Dict[str, Any], path: Optional[str] = None):
    provider = ask_provider_interactively()
    if provider:
        path = path if path else getcwd()
        generator = CICDGeneratorBase.build_generator(provider)
        params = {'tb_host': client.host, 'workspace_name': workspace['name'], 'tokens_url': f"{client.host}/{workspace['id']}/tokens"}
        warning_message = generator(path, params)
        click.echo(FeedbackManager.success_generate_cicd_config(provider=provider))
        if warning_message:
            click.echo(warning_message)
        click.echo(FeedbackManager.success_cicd())
