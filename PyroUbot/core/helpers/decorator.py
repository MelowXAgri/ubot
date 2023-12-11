from pyrogram.enums import ChatType

from PyroUbot import OWNER_ID, bot, ubot


async def get_private_and_group_chats(client):
    pm_chats = []
    gc_chats = []

    async for dialog in client.get_dialogs(limit=None):
        try:
            if dialog.chat.type == ChatType.PRIVATE:
                pm_chats.append(dialog.chat.id)
            elif dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                gc_chats.append(dialog.chat.id)
        except Exception as e:
            print(f"Error: {e}")

    return pm_chats, gc_chats


async def install_my_peer(client):
    pm_chats, gc_chats = await get_private_and_group_chats(client)
    client_id = client.me.id
    client._get_my_peer[client_id] = {"pm": pm_chats, "gc": gc_chats}


async def installPeer():
    try:
        for client in ubot._ubot:
            await install_my_peer(client)
    except Exception:
        pass
    await bot.send_message(OWNER_ID, "✅ sᴇᴍᴜᴀ ᴘᴇᴇʀ_ɪᴅ ʙᴇʀʜᴀsɪʟ ᴅɪɪɴsᴛᴀʟʟ")
