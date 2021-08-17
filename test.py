import discord
from discord import channel
from discord.ext import commands
from discord.ext.commands import bot


intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix = "!", intents=intents)
@client.event
async def on_ready():
    print("Lets gooo")

@client.event
async def on_member_join(member):
    channel = client.get_channel(875706600273350698)
    await channel.send("Hello Testers")

@client.command()
async def hello(ctx):
    await ctx.send("Hello This is a sample bot by code")
@client.command()
async def bye(ctx):
    await ctx.send("Life is Epic!!")


client.run('ODc3MDQyNzMzMDQ5NTk4MDIy.YRs3sg.Jq-fcTHomeY9Q6-tQsRjHX-ua04')