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

import pytgpt.phind

bot = pytgpt.phind.PHIND()

plugin_category = "البوت"

@l313l.ar_cmd(pattern="سؤال(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**✎┊‌ بالرد على السؤال او بأضافة سؤال \n يعني تكتب (`.سؤال`) وبعده سؤالك وخلص 😌 \n\n مثال : \n `.سؤال من هو مخترع الكهرباء`**")
    
    if not zilzal and event.reply_to_msg_id and zzz.text:
        zelzal = zzz.text
    if not event.reply_to_msg_id:
        zelzal = event.pattern_match.group(1)

    zed = await edit_or_reply(event, "**✎┊‌اصبر حبيبي هسة يجاوبك 😁**")
    
    try:
        response = gpt(zelzal)
        malath = response
        if "another 8 seconds" in malath: 
            aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌اصبر حبيبي هسة يجاوبك 😘**") 
            await event.delete()
            return await borg.send_message(event.chat_id, aa)
        if "understanding" in malath: 
            aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
            await event.delete()
            return await borg.send_message(event.chat_id, aa)
        await zed.delete()
        await borg.send_message(event.chat_id, f"**السؤال : {zelzal}\n\n{malath}**\n\n───────────────────\n")
    except Exception as e:
        await zed.delete()
        await borg.send_message(event.chat_id, f"**خطأ : {str(e)}**\n\n───────────────────\n")

def gpt(message):
    return bot.chat(f'{message}')
