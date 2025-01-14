from random import randint
from time import sleep
from typing import Dict
import requests
from lgt.common.python.helpers import update_credentials, get_formatted_bot_name
from lgt.common.python.slack_client.web_client import SlackWebClient
from lgt_data.enums import StatusConnection
from lgt_data.model import UserWorkspace, SlackUser
from lgt_data.mongo_repository import UserMongoRepository, DedicatedBotRepository
from ..basejobs import BaseBackgroundJobData, BaseBackgroundJob
from .bot_stats_update import BotStatsUpdateJob, BotStatsUpdateJobData
from ..runner import BackgroundJobRunner
from loguru import logger as log
from pydantic import BaseModel

"""
Connect Slack Account
"""


class ConnectSlackAccountJobData(BaseBackgroundJobData, BaseModel):
    slack_email: str
    current_user_email: str
    code: str
    user_agent: str
    reconnect: bool


class ConnectSlackAccountJob(BaseBackgroundJob):
    @property
    def job_data_type(self) -> type:
        return ConnectSlackAccountJobData

    def exec(self, data: ConnectSlackAccountJobData):
        current_user = UserMongoRepository().get_by_email(data.current_user_email)
        slack_user = current_user.get_slack_user(data.slack_email)
        if not slack_user:
            slack_user = SlackUser()
            slack_user.email = data.slack_email
            current_user.slack_users.append(slack_user)
        slack_user.status = StatusConnection.IN_PROGRESS

        client = SlackWebClient('')
        code_confirmed_response = client.confirm_code(data.slack_email, data.code, data.user_agent)
        if code_confirmed_response.status_code != 200:
            log.warning(f'Unable to confirm code due to error: {code_confirmed_response.content}')
            slack_user.status = StatusConnection.FAILED
            UserMongoRepository().set(current_user.id,
                                      slack_users=[user.to_dic() for user in current_user.slack_users])
            return

        code_confirmed = code_confirmed_response.json().get('ok', False)
        if not code_confirmed:
            slack_user.status = StatusConnection.FAILED
            UserMongoRepository().set(current_user.id,
                                      slack_users=[user.to_dic() for user in current_user.slack_users])
            log.warning(f'Invalid code')
            return

        slack_user.cookies = client.client.cookies = code_confirmed_response.cookies.get_dict()

        workspaces_response = client.find_workspaces(data.user_agent)
        if workspaces_response.status_code != 200:
            slack_user.status = StatusConnection.FAILED
            UserMongoRepository().set(current_user.id,
                                      slack_users=[user.to_dic() for user in current_user.slack_users])
            log.warning(f'Unable to get workspaces due to error: {workspaces_response.content}')
            return
        if not workspaces_response.json().get('ok', False):
            slack_user.status = StatusConnection.FAILED
            log.warning(f'Unable to get workspaces due to error: {workspaces_response.content}')
            return

        UserMongoRepository().set(current_user.id,
                                  slack_users=[user.to_dic() for user in current_user.slack_users])

        log.info(f'{slack_user.email}: got workspaces data {workspaces_response.json()}')
        user_workspaces = next((user for user in workspaces_response.json()['current_teams']
                                if user['email'] == data.slack_email), {}).get('teams', [])
        user_workspaces = [UserWorkspace.from_dic(ws) for ws in user_workspaces]
        user_workspaces = sorted(user_workspaces, key=lambda ws: ws.domain)

        session = requests.Session()
        session.cookies = code_confirmed_response.cookies
        session.headers.update({'User-Agent': data.user_agent})
        for workspace in user_workspaces:
            sleep(randint(0, 5))
            if not workspace.magic_login_code:
                continue
            login_url = f"https://app.slack.com/t/{workspace.domain}/login/{workspace.magic_login_code}"
            magic_response = session.post(login_url, cookies=session.cookies, headers=session.headers)
            content = magic_response.content.decode('utf-8')
            start_token_index = content.find("xox")
            sliced_content = content[start_token_index:]
            end_token_index = sliced_content.find('"')
            token = sliced_content[:end_token_index]
            workspace.magic_login_url = login_url
            workspace.token = token
            workspace.domain = get_formatted_bot_name(workspace.domain)

        slack_user.cookies = session.cookies.get_dict()
        slack_user.workspaces = user_workspaces
        slack_user.status = StatusConnection.COMPLETE

        UserMongoRepository().set(current_user.id,
                                  slack_users=[user.to_dic() for user in current_user.slack_users])

        dedicated_bots_repository = DedicatedBotRepository()
        dedicated_bots = dedicated_bots_repository.get_user_bots(current_user.id)

        if data.reconnect:
            user_workspaces_map: Dict[str, UserWorkspace] = {workspace.name: workspace
                                                             for workspace in user_workspaces if workspace.token}
            for name, workspace in user_workspaces_map.items():
                formatted_name = get_formatted_bot_name(name)
                dedicated_bot = next(filter(lambda x: x.name == formatted_name and x.user_name == slack_user.email,
                                            dedicated_bots), None)
                if dedicated_bot:
                    dedicated_bot = update_credentials(dedicated_bot, workspace.token, slack_user.cookies)
                    dedicated_bots_repository.add_or_update(dedicated_bot)
                    BackgroundJobRunner.submit(BotStatsUpdateJob,
                                               BotStatsUpdateJobData(dedicated_bot_id=str(dedicated_bot.id)))
