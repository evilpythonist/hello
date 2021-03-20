import os
import dotenv
import datetime

import discord
from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user} ({bot.user.id}) is connected to {guild} ({guild.id})')


@bot.event
async def on_member_join(member: discord.Member):
    await member.create_dm()
    await member.dm_channel_send(f'Hello {member.name}')


@bot.event
async def on_message(msg: discord.Message):
    if msg.author == bot.user:
        return
    elif msg.attachments and msg.attachments[0].filename.endswith('.exe'):
        await msg.channel.send('no nie')
    elif msg.content == 'hello man':
        await msg.channel.send('hello there')
    else:
        await bot.process_commands(msg)


@bot.command(name='wiki', help='Returns link to wikipedia page')
async def wiki(ctx: commands.Context, *args):
    await ctx.send(f'https://en.wikipedia.org/wiki/{"_".join(args)}')


@bot.command(name='translate', help='Translates given word')
async def translate(ctx: commands.Context, *args):
    await ctx.send(f'https://translate.google.com/?sl=auto&tl=pl&text={"%20".join(args)}%0A&op=translate')


@bot.command(name='now', help='Returns formatted date')
async def now(ctx: commands.Context):
    await ctx.send(datetime.datetime.now().strftime('%H:%M %d.%m.%Y'))


bot.run(TOKEN)
