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
    
    #Command for ban members from server
    @commands.command()
    async def ban(ctx, member:discord.Member, * ,reason = None):
        await member.ban(reason = reason)
        print('[MEMBER BANNED]')
    
    #Command for unban users
    @commands.command()
    async def unban(ctx, *,member):
        banned_users = await ctx.guild.bans()
        member_name , member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name,user.discriminator) == (member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                print(f'[USER {user.mention} UNBANNED]')
                return
   

def setup(client):
    client.add_cog(Manager(client))

