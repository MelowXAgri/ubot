import asyncio
import os
from gc import get_objects

from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait
from pyrogram.types import *
from telegraph import upload_file

from PyroUbot import *


async def broadcast_group_cmd(client, message):
    msg = await message.reply("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ...", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")

    blacklist = await get_chat(client.me.id)

    done = 0
    failed = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            if dialog.chat.id in blacklist:
                continue

            try:
                await asyncio.sleep(2)
                if message.reply_to_message:
                    await send.copy(dialog.chat.id)
                else:
                    await client.send_message(dialog.chat.id, send)
                done += 1
            except FloodWait as e:
                await asyncio.sleep(e.value)
                if message.reply_to_message:
                    await send.copy(dialog.chat.id)
                else:
                    await client.send_message(dialog.chat.id, send)
                done += 1
            except Exception:
                failed += 1

    await msg.delete()
    return await message.reply(
        f"""
<b>❏ ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ sᴇʟᴇsᴀɪ</b>
<b> ├ ʙᴇʀʜᴀsɪʟ ᴋᴇ; {done} ɢʀᴏᴜᴘ</b>
<b> ╰ ɢᴀɢᴀʟ ᴋᴇ: {failed} ɢʀᴏᴜᴘ</b>
""",
        quote=True,
    )


async def broadcast_users_cmd(client, message):
    msg = await message.reply("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ...")

    done = 0
    failed = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            if dialog.chat.id == client.me.id:
                continue

            try:
                await asyncio.sleep(2)
                if message.reply_to_message:
                    await send.copy(dialog.chat.id)
                else:
                    await client.send_message(dialog.chat.id, send)
                done += 1
            except FloodWait as e:
                await asyncio.sleep(e.value)
                if message.reply_to_message:
                    await send.copy(dialog.chat.id)
                else:
                    await client.send_message(dialog.chat.id, send)
                done += 1
            except Exception:
                failed += 1

    await msg.delete()
    return await message.reply(
        f"""
<b>❏ ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ sᴇʟᴇsᴀɪ</b>
<b> ├ ʙᴇʀʜᴀsɪʟ ᴋᴇ; {done} ᴜsᴇʀs</b>
<b> ╰ ɢᴀɢᴀʟ ᴋᴇ: {failed} ᴜsᴇʀs</b>
""",
        quote=True,
    )


async def send_msg_cmd(client, message):
    if message.reply_to_message:
        chat_id = (
            message.chat.id if len(message.command) < 2 else message.text.split()[1]
        )
        try:
            if client.me.id != bot.me.id:
                if message.reply_to_message.reply_markup:
                    x = await client.get_inline_bot_results(
                        bot.me.username, f"get_send {id(message)}"
                    )
                    return await client.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id
                    )
        except Exception as error:
            return await message.reply(error)
        else:
            try:
                return await message.reply_to_message.copy(chat_id)
            except Exception as t:
                return await message.reply(f"{t}")
    else:
        if len(message.command) < 3:
            return await message.reply("ᴋᴇᴛɪᴋ ʏᴀɴɢ ʙᴇɴᴇʀ")
        chat_id, chat_text = message.text.split(None, 2)[1:]
        try:
            if "/" in chat_id:
                to_chat, msg_id = chat_id.split("/")
                return await client.send_message(
                    to_chat, chat_text, reply_to_message_id=int(msg_id)
                )
            else:
                return await client.send_message(chat_id, chat_text)
        except Exception as t:
            return await message.reply(f"{t}")


async def send_inline(client, inline_query):
    try:
        _id = int(inline_query.query.split()[1])
        m = [obj for obj in get_objects() if id(obj) == _id][0]

        if m.reply_to_message.photo:
            m_d = await m.reply_to_message.download()
            photo_tg = upload_file(m_d)
            cp = m.reply_to_message.caption
            text = cp if cp else ""
            hasil = [
                InlineQueryResultPhoto(
                    photo_url=f"https://telegra.ph/{photo_tg[0]}",
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    caption=text,
                ),
            ]
            os.remove(m_d)
        else:
            hasil = [
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            ]
        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=hasil,
        )
    except Exception as e:
        print("Terjadi kesalahan:", str(e))
