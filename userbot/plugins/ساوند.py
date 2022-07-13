import re
import asyncio
import calendar
import json
import os
from telethon import events
from asyncio.exceptions import TimeoutError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ExportChatInviteRequest
from userbot import iqthon
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import get_user_from_event, sanga_seperator
from bs4 import BeautifulSoup
from ..helpers.utils import _format
from datetime import datetime
from urllib.parse import quote
import barcode
import qrcode
import requests
from barcode.writer import ImageWriter
from bs4 import BeautifulSoup
from PIL import Image, ImageColor
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import iqthon
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from userbot.utils import admin_cmd
from ..helpers import AioHttp
from ..helpers.utils import _catutils, _format, reply_id
LOGS = logging.getLogger(__name__)
IQMOG = re.compile(
    "[" 
    "\U0001F1E0-\U0001F1FF"      "\U0001F300-\U0001F5FF"      "\U0001F600-\U0001F64F"   "\U0001F680-\U0001F6FF"  
    "\U0001F700-\U0001F77F"      "\U0001F780-\U0001F7FF"      "\U0001F800-\U0001F8FF"     "\U0001F900-\U0001F9FF"      "\U0001FA00-\U0001FA6F"  
    "\U0001FA70-\U0001FAFF"      "\U00002702-\U000027B0"      
    "]+")

def iqtfy(inputString: str) -> str:
    return re.sub(IQMOG, "", inputString)
@iqthon.on(admin_cmd(pattern="ساوند ([\s\S]*)",
    command=("ساوند", plugin_category),
    info={
        "header": "لتحميل الاغاني من ساوند كلود عبر الرابـط",
        "الاستـخـدام": "{tr}ساوند بالـرد ع رابـط",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```بالـرد على الرابـط ```**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**```بالـرد على الرابـط ```**")
        return
    chat = "@DeezerMusicBot"
    catevent = await edit_or_reply(event, "** جـارِ التحميـل من سـاوند كـلاود انتظـر قليلاً**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=595898211)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**•╎تحـقق من انـك لم تقـم بحظـر البوت @downloader_tiktok_bot .. ثم اعـد استخدام الامـر ...**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**...؟**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@iqthon.on(admin_cmd(pattern="ساوند ([\s\S]*)",
    command=("ساوند", plugin_category),
    info={
        "header": "لتحميل الاغاني من ساوند كلاود عبر الرابـط",
        "الاستـخـدام": "{tr}ساوند + رابط",
    },
)
async def iq(event):
    if event.fwd_from:
        return
    zedr = event.pattern_match.group(1)
    zelzal = "@DeezerMusicBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(zelzal, zedr)
    await tap[0].click(event.chat_id)
    await event.delete()
