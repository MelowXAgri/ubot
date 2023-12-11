from PyroUbot import *

__MODULE__ = "copy"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏᴘʏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}copy</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴘᴇsᴀɴ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇʟᴀʟᴜɪ ʟɪɴᴋ ᴍᴇʀᴇᴋᴀ
  """


@PY.BOT("copy")
@PY.TOP_CMD
async def _(client, message):
    await copy_bot_msg(client, message)


@PY.UBOT("copy")
async def _(client, message):
    await copy_ubot_msg(client, message)
