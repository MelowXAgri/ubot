from PyroUbot import *

__MODULE__ = "logo"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏɢᴏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}logo</code> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴇʙᴜᴀʜ ʟᴏɢᴏ ᴅᴇɴɢᴀɴ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴀɴᴅᴏᴍ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}blogo</code> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴇʙᴜᴀʜ ʟᴏɢᴏ ᴅᴇɴɢᴀɴ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʜɪᴛᴀᴍ  
"""


@PY.UBOT("logo")
@PY.TOP_CMD
async def _(client, message):
    await logo_cmd(client, message)


@PY.UBOT("blogo")
@PY.TOP_CMD
async def _(client, message):
    await logo_cmd(client, message)
