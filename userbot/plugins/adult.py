from telethon import events
import asyncio
#from userbot.utils import admin_cmd
from userbot.events import register 
from userbot import bot, CMD_HELP
from telethon.errors.rpcerrorlist import YouBlockedUserError
import os
try:
 import subprocess
except:
 os.system("pip install instantimage")



os.system("rm -rf *.jpeg")


def bruh(name):

    os.system("instantimage -q -s "+name)


@register(outgoing=True, pattern="^.gaana(?: |$)(.*)")
async def Epornerbot(gaana):
    if gaana.fwd_from:
        return
    song = gaana.pattern_match.group(1)
    chat = "@Epornerbot"
    link = f"{gaana}"
    await gaana.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await gaana.edit("`Downloading...Please wait`")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await gaana.edit("```Please unblock @Epornerbot and try again```")
              return
          await gaana.edit("`Sending Your Music...weit!😎`")
          await asyncio.sleep(3)
          await bot.send_file(gaana.chat_id, respond)
    await gaana.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await gaana.delete()
