import discord
import json
from discord.ext import commands

#Read prefixes from prefixes json file
def get_prefix(client,message):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

#Create bot
client = commands.Bot(command_prefix = get_prefix)

#Event that show bot is start
@client.event
async def on_ready():
    print('[BOT IS RUNNING]')

client.run('NzczNDc2NTA5Njk1NDc1NzIz.X6JyIg.8pZfUSSS04XlU3DKF5GMTaiun7E')
