import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('[BOT IS RUNNING]')

client.run('NzczNDc2NTA5Njk1NDc1NzIz.X6JyIg.8pZfUSSS04XlU3DKF5GMTaiun7E')
