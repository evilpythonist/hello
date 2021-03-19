import re
from discord import *
from commands import *


class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} connected')
    async def on_member_join(self,member:discord.Member):
        await member.create_dm()
        await member.dm_channel.send('Hello')
    async def on_message(self,message:discord.Message):
        if message.author == self.user:
            pass
        else:
            if message.attachments:
                match_exe = re.match(".+\.exe",message.attachments[0].filename)
                if match_exe:
                    await mute(message)
            match_command = re.search("(?=\$\w+ ?).*",message.content)
            if match_command:
                command,*args = re.sub(" +"," ",match_command.group(0)).split(" ")
                if command == "$wiki":
                    await wiki(message,args)
                elif command == "$now":
                    await now(message)
                elif command == "$give_permissions":
                    await give_permission(self, args,message)
                elif command == "$kick":
                    await kick(self, args)
                elif command == "$invite":
                    await invite(self,message)

intents = discord.Intents(messages=True, guilds=True,members=True)
client = CustomClient(intents=intents)
client.run(TOKEN)
