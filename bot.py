import discord
from discord.ext import commands

# Set up the bot with a command prefix
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Create the /inquisicion command
@bot.command()
async def inquisicion(ctx):
    await ctx.send('hello')

# Run the bot using your token
bot.run('')
