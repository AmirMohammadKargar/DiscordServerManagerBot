import discord
import json
import os
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

#Command for load cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

#Command for unload cogs
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

#Read all cogs
for filename in os.listdir('./cogs'):
    if filename.endwith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzczNDc2NTA5Njk1NDc1NzIz.X6JyIg.8pZfUSSS04XlU3DKF5GMTaiun7E')
