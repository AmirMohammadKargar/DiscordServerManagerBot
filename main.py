import discord
import json
import os
import datetime
from discord.ext import commands

#Read prefixes from prefixes json file
def get_prefix(client,message):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

#Create bot
client = commands.Bot(command_prefix = get_prefix)

#Event that show bot is starting
@client.event
async def on_ready():
    with open('logs.txt','a+') as f:
        now = datetime.datetime.now()
        f.write(f'\n[%s]->[BOT IS RUNNING]\n'%(now))
    print('[BOT IS RUNNING]')

#Event fo log join user        
async def on_member_join(member):
    with open('logs.txt','a+') as f:
        now = datetime.datetime.now()
        f.write(f'\n[%s]->[[member] HAS JOINED SERVER]\n'%(now))
    print(f'[[member] HAS JOINED SERVER]')

#Event for log remove user
@client.event
async def on_member_remove(member):
    now = datetime.datetime.now()
    with open('logs.txt','a+') as f:
        f.write(f'\n[%s]->[[member] HAS LEFTED SERVER]\n'%(now))
    print(f'[[member] HAS LEFTED SERVER]')

#Event that create defualt value for prefix when bot join server
@client.event
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '.'

    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

    now = datetime.datetime.now() 
    with open('logs.txt','a+') as f:
        f.write(f'\n[%s]->[ADD DEFAULT PREFIX]\n'%(now))
    
    print(f'[ADD DEFAULT PREFIX]')

#Event that remove prefix from json file when bot remove from server
@client.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))

    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

    now = datetime.datetime.now() 
    with open('logs.txt','a+') as f:
        f.write(f'\n[%s]->[DELETE PREFIX]\n'%(now))
    
    print(f'[DELETE PREFIX]')

#Command for change prefix
@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

    now = datetime.datetime.now() 
    with open('logs.txt','a+') as f:
        f.write(f'\n[%s]->[PREFIX CHANGED TO %s]\n'%(now,prefix))

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
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('')
