from PyroUbot import *

__MODULE__ = "quotly"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ǫᴜᴏᴛʟʏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}q</code> [ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴇxᴛ ᴍᴇɴᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ
"""


@PY.UBOT("q")
@PY.TOP_CMD
async def _(client, message):
    await quotly_cmd(client, message)
