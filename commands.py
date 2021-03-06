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
    
async def give_permission(client,id,message):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    overwrite.read_messages = True
    await message.channel.set_permissions(get(client.guilds[0].members, id=int(id[0])),overwrite=overwrite)
    
async def kick(client,id):
    member = get(client.guilds[0].members, id=int(id[0]))
    member.kick()
    
async def get_id(client:Client,message:Message):
   for member in message.mentions:
       await message.channel.send(member.name +" : "+str(member.id))
    
async def invite(client:Client,message:Message):
    await message.channel.send("https://discord.gg/r8w7XAgH2E")
    
async def new_channel(client:Client,args):
    await client.guilds[0].create_text_channel(args[0])
    
async def delete_channel(client:Client,args):
    ch= discord.utils.get(client.guilds[0].channels, name=args[0])
    await ch.delete()
    
async def new_voice_channel(client:Client,args):
    await client.guilds[0].create_voice_channel(args[0])
