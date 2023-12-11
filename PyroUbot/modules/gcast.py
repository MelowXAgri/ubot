from PyroUbot import *

__MODULE__ = "gcast"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴄᴀsᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ucast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴜsᴇʀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}gcast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}send</code> [ᴜsᴇʀɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ᴛᴇxᴛ/ʀᴇᴘʟʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ ᴜsᴇʀ/ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟd
"""


@PY.UBOT("gcast")
@PY.TOP_CMD
async def _(client, message):
    await broadcast_group_cmd(client, message)


@PY.UBOT("ucast")
@PY.TOP_CMD
async def _(client, message):
    await broadcast_users_cmd(client, message)


@PY.BOT("send")
@PY.UBOT("send")
@PY.TOP_CMD
async def _(client, message):
    await send_msg_cmd(client, message)


@PY.INLINE("^get_send")
@INLINE.QUERY
async def _(client, inline_query):
    await send_inline(client, inline_query)
