import discord
import asyncio
from discord.ext import commands


bot = commands.Bot(command_prefix="!", description="BigBot")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello world!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def say(ctx, *, something):
    await ctx.send(something)


@bot.command()
async def mention(ctx):
    await ctx.send(ctx.author.mention)


@bot.group(invoke_without_subcommand=True)
async def server(ctx):
    em = discord.Embed(title=ctx.guild.name, description="ID:" + str(ctx.guild.id), colour=discord.Colour.green())
    em.set_image(url=str(ctx.guild.icon_url))
    await ctx.send(embed=em)

@server.command(name="name")
async def server_name(ctx):
    await ctx.send("Server Name: " + ctx.guild.name)


@server.command(name="owner")
async def server_owner(ctx):
    await ctx.send("Server Owner: " + str(ctx.guild.owner))


@server.command(name="region")
async def server_region(ctx):
    await ctx.send("Server Region: " + str(ctx.guild.region))


@server.command(name="afk")
async def server_afk(ctx):
    await ctx.send("AFK Timeout: " + str((ctx.guild.afk_timeout)//60) + " min")


@server.command(name="verification")
async def server_verification(ctx):
    await ctx.send("Server Verification Level: " + str(ctx.guild.verification_level))


@bot.event
async def on_member_join(member):
    guild = member.guild
    await member.send("Welcome to {}!".format(guild.name))



bot.run("NDIzMjI2NTY0Nzk3MjY3OTY4.DYngQg.a9KX8UVOhajRc3mC-td_2Cag5KQ")
