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
client = CustomClient()
client.run(TOKEN)
