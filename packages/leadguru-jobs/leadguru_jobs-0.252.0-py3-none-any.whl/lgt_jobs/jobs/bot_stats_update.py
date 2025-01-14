from abc import ABC
from typing import Optional
from lgt.common.python.slack_client.web_client import SlackWebClient
from lgt_data.mongo_repository import BotMongoRepository, DedicatedBotRepository
from pydantic import BaseModel
from lgt_data.analytics import get_bots_aggregated_analytics
from lgt.common.python.lgt_logging import log
from lgt.common.python.enums.slack_errors import SlackErrors
from ..basejobs import BaseBackgroundJob, BaseBackgroundJobData

"""
Update bots statistics
"""


class BotStatsUpdateJobData(BaseBackgroundJobData, BaseModel):
    dedicated_bot_id: Optional[str]
    bot_name: Optional[str]


class BotStatsUpdateJob(BaseBackgroundJob, ABC):
    @property
    def job_data_type(self) -> type:
        return BotStatsUpdateJobData

    def exec(self, data: BotStatsUpdateJobData):
        if data.dedicated_bot_id:
            bots_rep = DedicatedBotRepository()
            bot = bots_rep.get_by_id(data.dedicated_bot_id)
        else:
            bots_rep = BotMongoRepository()
            bot = bots_rep.get_by_id(data.bot_name)

        if not bot.invalid_creds:
            return

        received_messages, filtered_messages = get_bots_aggregated_analytics(bot_ids=[bot.id])
        client = SlackWebClient(bot.token, bot.cookies)
        if not bot.token or not bot.cookies:
            log.warning(f"[BotStatsUpdateJob]: Bot {bot.id} has no credentials.")
            bot.invalid_creds = True
            bots_rep.add_or_update(bot)
            return
        channels_response = client.channels_list()
        if not channels_response['ok']:
            if channels_response.get("error") == SlackErrors.INVALID_AUTH:
                bot.invalid_creds = True
                bots_rep.add_or_update(bot)
            else:
                log.warning(f"[BotStatsUpdateJob]: Error during update bot {bot.id} stats. Error: {channels_response}")
            return
        channels = channels_response['channels']
        connected_channels = 0
        channels_users = {}
        active_channels = {}
        users_count = 0
        for channel in channels:
            if channel['is_member']:
                active_channels[channel['id']] = channel['name']
                connected_channels += 1
            num_members = channel.get('num_members', 0)
            channels_users[channel['id']] = num_members
            users_count += num_members

        bot.active_channels = active_channels
        bot.messages_received = received_messages.get(bot.name, 0)
        bot.messages_filtered = filtered_messages.get(bot.name, 0)
        bot.connected_channels = connected_channels
        bot.channels = len(channels)
        bot.channels_users = channels_users
        bot.users_count = users_count
        if bot.recent_messages is None:
            bot.recent_messages = []

        # save only last 50 messages
        bot.recent_messages = bot.recent_messages[-50:]
        bots_rep.add_or_update(bot)
