from .. import *


@PY.UBOT("catur")
@PY.TOP_CMD
async def _(client, message):
    await catur_cmd(client, message)
