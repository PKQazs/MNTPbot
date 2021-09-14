import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
bot.run('ODg3Mzg4MjU3NjM2MjAwNDg4.YUDatw.mPaDB8P20aGR--kFLroQjdgAzMc')  
# Don't reveal your bot token, regenerate it asap if you do