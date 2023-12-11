from PyroUbot import *

__MODULE__ = "anime"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴɪᴍᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}wall</code>
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}waifu</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴀɴɪᴍᴇ ʀᴀɴᴅᴏᴍ
"""


@PY.UBOT("wall|waifu")
@PY.TOP_CMD
async def _(client, message):
    await anime_cmd(client, message)
