from PyroUbot import *


@PY.UBOT("pw")
@PY.TOP_CMD
async def _(client, message):
    await gen_password(client, message)
