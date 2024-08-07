import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"

@l313l.ar_cmd(pattern="سؤال(?: |$)(.*)")
async def zelzal_gpt(event):
    question = event.pattern_match.group(1)
    reply_msg = await event.get_reply_message()
    chat = "@BotUsername"  # ضع هنا اسم المستخدم للبوت الذي تريد التعامل معه

    if not question and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**✎┊‌ بالرد على السؤال او بأضافة سؤال \n يعني تكتب (`.سؤال`) وبعده سؤالك وخلص 😌 \n\n مثال : \n `.سؤال من هو مخترع الكهرباء`**")

    if not question and event.reply_to_msg_id and reply_msg.text:
        question = reply_msg.text
    elif not event.reply_to_msg_id:
        question = event.pattern_match.group(1)

    response_message = await edit_or_reply(event, "**✎┊‌اصبر حبيبي هسة يجاوبك 😁**")

    async with borg.conversation(chat) as conv:
        try:
            await conv.send_message(question)
            response = await conv.get_response()
            answer = response.text

            if "another 8 seconds" in response.text:
                message = answer.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌اصبر حبيبي هسة يجاوبك 😘**")
                await event.delete()
                return await borg.send_message(event.chat_id, message)

            await asyncio.sleep(5)
            follow_up_response = await conv.get_response()
            answer = follow_up_response.text

            if "understanding" in follow_up_response.text:
                message = answer.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**")
                await event.delete()
                return await borg.send_message(event.chat_id, message)

            await response_message.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {question}\n\n{answer}**\n\n───────────────────\n")
        except YouBlockedUserError:
            await borg(unblock(chat))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(question)
            response = await conv.get_response()
            answer = response.text

            if "another 8 seconds" in response.text:
                message = answer.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌ اصبر حبيبي هسة يجاوبك 😁**")
                await event.delete()
                return await borg.send_message(event.chat_id, message)

            await asyncio.sleep(5)
            follow_up_response = await conv.get_response()
            answer = follow_up_response.text

            if "understanding" in follow_up_response.text:
                message = answer.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**")
                await event.delete()
                return await borg.send_message(event.chat_id, message)

            if "Please wait a moment" in follow_up_response.text:
                await asyncio.sleep(5)
                follow_up_response = await conv.get_response()
                answer = follow_up_response.text

            await response_message.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {question}\n\n{answer}**\n\n───────────────────\n")
