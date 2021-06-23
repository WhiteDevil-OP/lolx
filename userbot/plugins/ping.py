import asyncio
from datetime import datetime

from . import mention


@bot.on(admin_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"**Pɪɴɢ**!\n`{ms} ᴍs`\nMʏ ᴏᴘ ᴍᴀsᴛᴇʀ: {mention}")



CMD_HELP.update(
    {
        "ping": "**Plugin :** `ping`\
    \n\n•  **Syntax :** `.ping`\
    \n•  **Function : **__Shows you the ping speed of server__\
    "
    }
)
