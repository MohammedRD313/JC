import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import pytgpt.phind
from gpt import gpt 
bot = pytgpt.phind.PHIND()

def gpt(message):
    return bot.chat(f'{message}')

@events.register(events.NewMessage(pattern=r"^\.سؤال(?: |$)(.*)"))
async def zelzal_gpt(event):
    zelzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    if not zelzal and not event.reply_to_msg_id:
        return await event.reply("بالرد على السؤال او بإضافة سؤال\nاكتب (.سؤال) وبعده سؤالك.")
    if not zelzal and event.reply_to_msg_id and zzz.text:
        zelzal = zzz.text
    zed = await event.reply("اصبر قليلاً، جاري الإجابة...")
    try:
        response = gpt(zelzal)
        await zed.delete()
        await event.reply(f"السؤال: {zelzal}\n\nالإجابة: {response}")
    except Exception as e:
        await zed.delete()
        await event.reply(f"حدث خطأ: {e}")
