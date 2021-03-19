from datetime import datetime

from discord import Message


async def wiki(message:Message,args):
    str = ""
    for arg in args:
        str += arg + "_"
    str = str[0:len(str) - 1]
    await message.channel.send("https://pl.wikipedia.org/wiki/" + str)
async def now(message:Message):
    await message.channel.send(datetime.now())