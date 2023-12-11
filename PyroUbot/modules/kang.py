from PyroUbot import *

__MODULE__ = "kang"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴀɴɢ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}kang</code> [ʀᴇᴘʟʏ ᴛᴏ ɪᴍᴀɢᴇ/sᴛɪᴄᴋᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴅᴀɴ ᴄᴏsᴛᴜᴍ ᴇᴍᴏᴊɪ sᴛɪᴄᴋᴇʀ ᴋᴇ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ
"""


@PY.UBOT("kang")
@PY.TOP_CMD
async def _(client, message):
    await kang_cmd(client, message)
