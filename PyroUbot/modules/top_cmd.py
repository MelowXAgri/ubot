from PyroUbot import *


@PY.UBOT("topcmd", FILTERS.OWNER)
async def _(client, message):
    await get_top_module(client, message)
