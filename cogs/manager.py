import discord
from discord.ext import commands

class Manager(commands.Cog):
    
    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency*1000)}ms')
        print('[PING COMMAND]')
    
    #Command for kick members from server
    @commands.command()
    async def kick(ctx, member:discord.Member, * ,reason = None):
        await member.kick(reason = reason)
        print('[MEMBER KICKED]')
        
def setup(client):
    client.add_cog(Manager(client))

