from PyroUbot import *

__MODULE__ = "vctools"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟꜱ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}startvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stopvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋʜɪʀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.
"""


@PY.UBOT("startvc")
@PY.TOP_CMD
async def _(client, message):
    await start_vctools(client, message)


@PY.UBOT("stopvc")
@PY.TOP_CMD
async def _(client, message):
    await stop_vctools(client, message)
