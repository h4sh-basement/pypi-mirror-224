from typing import Any, Dict, Union

from bidict import bidict
from pydantic import BaseModel, Field

from .nonebot.utils import Bot, MessageEvent, TG_Bot, KOOK_Bot, DISCORD_Bot, OB11_Bot
from ..chatbot.bard import Bard_Bot
from ..chatbot.chatgpt_web import ChatGPT_web_Bot
from ..chatbot.claude_ai import Claude_Bot
from ..chatbot.newbing import Newbing_Bot
from ..chatbot.poe import Poe_Bot
from ..chatbot.slack_claude import Slack_Claude_Bot
from ..chatbot.spark_desk import SparkBot
from ..chatbot.sydneybing import SydneyBing_Bot
from ..chatbot.tongyiqianwen import TongYiQianWen_Bot
from ..common.mytypes import CommonUserInfo, BotInfo, BotData
from ..common.user_data import common_users

CHATBOT = Union[
    SparkBot,
    Newbing_Bot,
    SydneyBing_Bot,
    ChatGPT_web_Bot,
    Slack_Claude_Bot,
    Poe_Bot,
    Bard_Bot,
    TongYiQianWen_Bot,
]
BOT_DICT = {
    "spark desk": SparkBot,
    "bing": Newbing_Bot,
    "sydneybing": SydneyBing_Bot,
    "chatgpt web": ChatGPT_web_Bot,
    "slack claude": Slack_Claude_Bot,
    "claude ai": Claude_Bot,
    "poe chatgpt": Poe_Bot,
    "poe claude": Poe_Bot,
    "poe claude-2-100k": Poe_Bot,
    "poe chatgpt4": Poe_Bot,
    "bard": Bard_Bot,
    "通义千问": TongYiQianWen_Bot,
}

GET_HANDLERS = {
    OB11_Bot: lambda event: str(event.reply.message_id),
    TG_Bot: lambda event: str(event.reply_to_message.message_id + event.from_.id),
    KOOK_Bot: lambda event: str(event.msg_id),
    DISCORD_Bot: lambda event: str(event.reply.id),
}

SEND_HANDLERS = {
    OB11_Bot: lambda reply, event: str(reply["message_id"]),
    TG_Bot: lambda reply, event: str(reply.message_id + event.from_.id),
    KOOK_Bot: lambda reply, event: str(reply.msg_id),
    DISCORD_Bot: lambda reply, event: str(reply.id),
}


class Bot_Links(BaseModel):
    msg_bot_dict: bidict[BotInfo, Any] = Field(None, description="储存信息和chatbot的双向dict")
    bot_dict: Dict[BotInfo, Any] = Field(None, description="储存用户和其chatbot的dict")

    def __init__(self, **data):
        super().__init__(**data)
        self.msg_bot_dict: bidict = data.get("msg_bot_dict") or bidict()
        self.bot_dict: Dict[BotInfo, Any] = data.get("bot_dict") or bidict()


def get_message_id_by_get(bot: Bot, event: MessageEvent) -> str:
    handler = GET_HANDLERS.get(type(bot))
    if handler:
        return handler(event)


def get_message_id_by_send(
        event: MessageEvent,
        reply: any,
        bot: Bot,
) -> str:
    handler = SEND_HANDLERS.get(type(bot))
    if handler is not None:
        return handler(reply, event)
    return ""


class Temp_Bots(BaseModel):
    users: Dict[CommonUserInfo, Bot_Links] = Field(
        None, description="储存运行中创建和使用的chatbot"
    )

    def __init__(self, **data):
        super().__init__(**data)
        self.users: Dict[CommonUserInfo, Bot_Links] = data.get("users") or {}

    def set_bot_msgid(
            self,
            common_userinfo: CommonUserInfo,
            chatbot: CHATBOT,
            bot: Bot,
            event: MessageEvent,
            reply: any,
    ):
        botlinks: Bot_Links = self.get_bot_links(common_userinfo)
        if chatbot:
            botlinks.msg_bot_dict.inv[chatbot] = get_message_id_by_send(
                event, reply, bot
            )
        else:
            raise Exception("没有这个bot")

    def get_bot_by_msgid(
            self,
            common_userinfo: CommonUserInfo,
            bot: Bot,
            event: MessageEvent,
            kook_msgid: str = "",
    ):
        botlinks: Bot_Links = self.get_bot_links(common_userinfo)
        if kook_msgid:
            message_id = kook_msgid
        else:
            message_id = get_message_id_by_get(bot, event)
        if str(message_id) in botlinks.msg_bot_dict.keys():
            return botlinks.msg_bot_dict[str(message_id)]
        else:
            raise Exception("没有这个messageid对应的bot")

    def get_bot_by_text(
            self, common_userinfo: CommonUserInfo, text: str
    ) -> tuple[str, CHATBOT]:
        """由原始的命令加bot名加问题得到问题和可调用的chatbot"""
        from ..common.load_config import PRIVATE_COMMAND, PUBLIC_COMMAND
        try:
            botinfo, botdata = common_users.get_bot_by_text(common_userinfo, text)
        except Exception:
            raise

        question = text.replace(f"{PRIVATE_COMMAND}{botinfo.nickname}", "").replace(
            f"{PUBLIC_COMMAND}{botinfo.nickname}", ""
        )
        try:
            bot = self.get_bot_by_botinfo(
                common_userinfo=common_userinfo, bot_info=botinfo
            )
        except:
            self.load_user_bot(
                common_userinfo=common_userinfo, botinfo=botinfo, botdata=botdata
            )
            bot = self.get_bot_by_botinfo(
                common_userinfo=common_userinfo, bot_info=botinfo
            )

        return question, bot

    def load_user_bot(
            self, common_userinfo: CommonUserInfo, botinfo: BotInfo, botdata: BotData
    ):
        """由本地bot数据load到tempbots中的可调用实例"""
        bot_links: Bot_Links = self.get_bot_links(common_userinfo=common_userinfo)

        bot_links.bot_dict[botinfo] = BOT_DICT.get(botdata.source)(
            common_userinfo=common_userinfo, bot_info=botinfo, bot_data=botdata
        )

    def add_new_bot(
            self,
            common_userinfo: CommonUserInfo,
            botinfo: BotInfo,
            botdata: BotData,
    ):
        common_users.add_new_bot(
            common_userinfo=common_userinfo,
            botinfo=botinfo,
            botdata=botdata,
        )
        self.load_user_bot(
            common_userinfo=common_userinfo, botinfo=botinfo, botdata=botdata
        )

    def get_bot_by_botinfo(self, common_userinfo: CommonUserInfo, bot_info: BotInfo):
        bot_links: Bot_Links = self.get_bot_links(common_userinfo=common_userinfo)
        if bot_info in bot_links.bot_dict.keys():
            return bot_links.bot_dict[bot_info]
        else:
            raise Exception("Temp_Bots中没有这个bot")

    def get_bot_links(self, common_userinfo: CommonUserInfo):
        if common_userinfo in self.users.keys():
            return self.users[common_userinfo]
        else:
            self.users[common_userinfo] = Bot_Links()
            return self.users[common_userinfo]


temp_bots = Temp_Bots()
