from datetime import datetime

import discord
from discord import Message, Client, Member
from discord.utils import get


async def wiki(message:Message,args):
    str = ""
    for arg in args:
        str += arg + "_"
    str = str[0:len(str) - 1]
    await message.channel.send("https://pl.wikipedia.org/wiki/" + str)
async def now(message:Message):
    await message.channel.send(datetime.now())

async def mute(message:Message):
    await message.channel.send(content='No exe')
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = True
    await message.channel.set_permissions(message.author,overwrite=overwrite)
    
async def give_permission(user,message:Message):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    overwrite.read_messages = True
    await message.channel.set_permissions(user,overwrite=overwrite)
    
async def give_permission(client,id):
    print(client.guilds[0].members)
    member =  get(client.guilds[0].members, id=int(id[0]))
async def kick(client,id):
    member = get(client.guilds[0].members, id=int(id[0]))
    member.kick()
async def invite(client:Client,message:Message):
    await message.channel.send("https://discord.gg/r8w7XAgH2E")
