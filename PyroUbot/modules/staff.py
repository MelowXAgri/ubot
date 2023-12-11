from PyroUbot import *

__MODULE__ = "staff"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀꜰꜰ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}staff</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴅᴀꜰᴛᴀʀ sᴇᴍᴜᴀ ᴀᴅᴍɪɴ ᴅɪᴅᴀʟᴀᴍ ɢʀᴜᴘ
"""


@PY.UBOT("staff")
@PY.TOP_CMD
async def _(client, message):
    await staff_cmd(client, message)
