import re
import discord
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
            match = re.search("(?=\$\w+ ?).*",message.content)
            command,*args = re.sub(" +"," ",match.group(0)).split(" ")
            if command == "$wiki":
                await wiki(message,args)
            elif command == "$now":
                await now(message)
                
client = CustomClient()
client.run(TOKEN)
