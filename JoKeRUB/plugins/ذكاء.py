""" 
# فريق العقرب 
# علوش @ZS_SQ
# محمد @Zo_r0
"""

import requests
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from JoKeRUB import l313l
from . import l313l
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"


@l313l.ar_cmd(pattern="سؤال(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@ScorGPTbot"
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**✎┊‌ بالرد على السؤال او بأضافة سؤال \n يعني تكتب (`.سؤال`) وبعده سؤالك وخلص 😌 \n\n مثال : \n `.سؤال من هو مخترع الكهرباء`**")
    if not zilzal and event.reply_to_msg_id and zzz.text: 
        zelzal = zzz.text
    if not event.reply_to_msg_id: 
        zelzal = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**✎┊‌اصبر حبيبي هسة يجاوبك 😁**")
    async with borg.conversation(chat) as conv:
        try:
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: 
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌اصبر حبيبي هسة يجاوبك 😘**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            l313l = await conv.get_response()
            malath = l313l.text
            if "understanding" in l313l.text: 
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {zelzal}\n\n{malath}**\n\n───────────────────\n")
        except YouBlockedUserError: 
            await zedub(unblock("ScorGPTbot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text:
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌ اصبر حبيبي هسة يجاوبك 😁**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            l313l = await conv.get_response()
            malath = l313l.text
            if "understanding" in l313l.text:
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            if "Please wait a moment" in l313l.text:
                await asyncio.sleep(5)
                l313l = await conv.get_response()
                malath = l313l.text
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {zelzal}\n\n{malath}**\n\n───────────────────\n")

