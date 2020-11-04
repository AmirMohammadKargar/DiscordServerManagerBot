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

#Event that create defualt value for prefix when bot join server
@client.event
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '.'

    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)
    
    print(f'[ADD DEFAULT PREFIX]')

#Event that remove prefix from json file when bot remove from server
@client.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))

    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

    print(f'[DELETE PREFIX]')

#Command for change prefix
@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

    print(f'[PREFIX CHANGED TO {prefix}]')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

client.run('NzczNDc2NTA5Njk1NDc1NzIz.X6JyIg.8pZfUSSS04XlU3DKF5GMTaiun7E')
