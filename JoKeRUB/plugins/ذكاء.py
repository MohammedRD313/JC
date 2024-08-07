import asyncio
from telethon import events
from telethon.errors import FloodWaitError, YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from JoKeRUB import l313l
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "البوت"

@l313l.ar_cmd(pattern="سؤال(?: |$)(.*)")
async def zelzal_gpt(event):
    question = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@ScorGPTbot"

    if not question and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**✎┊‌ بالرد على السؤال او بأضافة سؤال \n يعني تكتب (`.سؤال`) وبعده سؤالك وخلص 😌 \n\n مثال : \n `.سؤال من هو مخترع الكهرباء`**")
    
    if not question and event.reply_to_msg_id and reply_message.text: 
        question = reply_message.text
    
    if not event.reply_to_msg_id: 
        question = event.pattern_match.group(1)
    
    response_msg = await edit_or_reply(event, "**✎┊‌اصبر حبيبي هسة يجاوبك 😁**")

    async with borg.conversation(chat) as conv:
        try:
            await conv.send_message(question)
            response = await conv.get_response()
            print(f"Received initial response: {response.text}")
            
            if "another 8 seconds" in response.text: 
                msg = response.text.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌اصبر حبيبي هسة يجاوبك 😘**") 
                await event.delete()
                return await borg.send_message(event.chat_id, msg)
            
            await asyncio.sleep(5)
            final_response = await conv.get_response()
            print(f"Received final response: {final_response.text}")
            
            if "understanding" in final_response.text: 
                msg = final_response.text.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, msg)
            
            await response_msg.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {question}\n\n{final_response.text}**\n\n───────────────────\n")
        except YouBlockedUserError: 
            print("YouBlockedUserError: Trying to unblock and resend")
            await borg(UnblockRequest("ScorGPTbot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(question)
            response = await conv.get_response()
            print(f"Received initial response after unblock: {response.text}")
            
            if "another 8 seconds" in response.text:
                msg = response.text.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**✎┊‌ اصبر حبيبي هسة يجاوبك 😁**") 
                await event.delete()
                return await borg.send_message(event.chat_id, msg)
            
            await asyncio.sleep(5)
            final_response = await conv.get_response()
            print(f"Received final response after unblock: {final_response.text}")
            
            if "understanding" in final_response.text:
                msg = final_response.text.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, msg)
            
            await response_msg.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {question}\n\n{final_response.text}**\n\n───────────────────\n")
        except FloodWaitError as e:
            print(f"FloodWaitError: Waiting for {e.seconds} seconds")
            await asyncio.sleep(e.seconds)
            await zelzal_gpt(event)
        except Exception as e:
            print(f"Exception: {str(e)}")
            await response_msg.edit(f"**حدث خطأ:** {str(e)}")
