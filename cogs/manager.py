import discord
import os.path
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
    async def kick(self,ctx, member:discord.Member, * ,reason = None):
        await member.kick(reason = reason)
        print('[MEMBER KICKED]')
    
    #Command for ban members from server
    @commands.command()
    async def ban(self,ctx, member:discord.Member, * ,reason = None):
        await member.ban(reason = reason)
        print('[MEMBER BANNED]')
    
    #Command for unban users
    @commands.command()
    async def unban(self,ctx, *,member):
        banned_users = await ctx.guild.bans()
        member_name , member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name,user.discriminator) == (member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                print(f'[USER {user.mention} UNBANNED]')
                return

    #Command for show server information 
    @commands.command()
    async def info(self,ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
        owner = str(ctx.guild.owner)
        Id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        icon = str(ctx.guild.icon_url)
        member_count = str(ctx.guild.member_count)

        embed = discord.Embed(
            title = name + ' Server information',
            description = description,
            color = discord.Color.red()
            )
        embed.set_thumbnail(url=icon)
        embed.add_field(name='Owner',value=owner,inline=True)      
        embed.add_field(name='Id',value=Id,inline=True)
        embed.add_field(name='Region',value=region,inline=True)

        embed.add_field(name='Members',value=member_count,inline=True)
        await ctx.send(embed=embed)

    #Command for delete message
    @commands.command()
    async def clear(self,ctx,amount = 5):
        await ctx.channel.purge(limit = amount)
    
    #Command for showing log from log file
    @commands.command()
    async def log(self,ctx):
        with open(os.path.dirname(__file__)+'/../logs.txt','r') as f:
            data = f.read()
            await ctx.send(data)

def setup(client):
    client.add_cog(Manager(client))

