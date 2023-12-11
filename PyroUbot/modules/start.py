from .. import *


@PY.UBOT("ping")
@PY.TOP_CMD
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)
