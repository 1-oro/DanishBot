
from telethon import events
import asyncio


@borg.on(events.NewMessage(pattern=r"cool(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 16)
    input_str = event.pattern_match.group(1)
    if input_str == "cool":
        await event.edit(input_str)
        animation_chars = [
            "CooL",
            "🤩🤩",
            "cOOl",
            "🤩🤩",
            "🆒",
            "#coO0l",
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])