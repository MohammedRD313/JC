import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from ..core.managers import edit_delete, edit_or_reply

# استيراد دالة gpt من الملف gpt.py
from gpt import gpt

plugin_category = "البوت"

@l313l.ar_cmd(pattern="سؤال(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**✎┊‌ بالرد على السؤال او بإضافة سؤال\nاكتب (.سؤال) وبعده سؤالك وخلص 😌\n\nمثال: \n`.سؤال من هو مخترع الكهرباء`**")
    if not zilzal and event.reply_to_msg_id and zzz.text:
        zelzal = zzz.text
    if not event.reply_to_msg_id:
        zelzal = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**✎┊‌اصبر حبيبي هسة يجاوبك 😁**")
    try:
        response = gpt(zilzal)
        await zed.delete()
        await event.reply(f"**السؤال: {zelzal}\n\nالإجابة: {response}**\n\n───────────────────\n")
    except Exception as e:
        await zed.delete()
        await event.reply(f"حدث خطأ: {e}")
