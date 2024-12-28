# This example requires the 'members' and 'message_content' privileged intents to function.

import secrets
import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


users = [ 'gopollo', '777juicy777', 'skinalived', 'erpepe_123', 'cazperr', 'imoverit.', 'tstastan', 'crazysmoker_', 'sugakick', 'arkie0000', 'shinuhi', 'fo.x.0', 'jdjdjeiexnrei', 'kriyze', 'simiuno', 'hobbitmati', 'lezzox', 'sword1', 'hbelze', 'hugosa', 'de_beukeler', 'kyr1t0', 'eusebioponte1000', 'wositodelasalada', 'samus225', 'avkern', 'snilemb', 'barbadaco', 'damon4401', 'talentedcapy', 'protuva', 'el7raq', '.r1wo', 'bt_king', 'xtoxic7x', 'ruudyx', 'ksmfoly', 'p1stoo', 'michaelb.jordan.', 'rubo0695', 'gary.2', 'karamelon', 'wavi_', 'jossny', 'stitch_gang', 'lariostrina', 'alek.04', 'deptox', 'atufeitor3000', 'rookie32.', '.balcho', 'zak16', '.cornago']


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def inquisicion(ctx):
    """Adds two numbers together."""
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name="human")
    if not role:
        await ctx.send(f"The role '{role_name}' does not exist!")
        return

    for username in users:
        # Find the user by username
        member = discord.utils.get(guild.members, name=username)

        if member:
            # Add the role to the user
            await member.add_roles(role)
            await ctx.send(f"Assigned 'human' role to {member.name}.")
        else:
            await ctx.send(f"User '{username}' not found.")


    await ctx.send("todo los usuarios han sido añadidos")

role_name = "human"
@bot.command()
async def mueltos(ctx):
    # Get the guild (server) where the command was called
    guild = ctx.guild
    # Get the role by name
    role = discord.utils.get(guild.roles, name=role_name)

    if not role:
        await ctx.send(f"The role '{role_name}' does not exist!")
        return

    # List of members who do not have the 'human' role
    members_without_role = [member for member in guild.members if role not in member.roles]

    if not members_without_role:
        await ctx.send(f"All members have the '{role_name}' role.")
    else:
        names = [f"<@{member.id}>" for member in members_without_role]
        await ctx.send(f"Members without the '{role_name}' role: {'\n'.join(names)}")



names_without_human_role = [ 'NecroSwag', 'no', 'Troika', 'eZteb4n', 'Rain', 'MB^_^Myears', 'Valenzuela', 'Baumplatte', 'WhoDisNewPhone', 'HackHoff', 'Heca', 'Gizakor', 'LordAlphis', 'Swampy', 'Najzar', 'Paxt', 'Samole', 'Rank', 'Beru', 'Blacky34', 'Shadovv', 'Sheeesh', 'TP | POU', 'mentally gone', 'antoniocaro29', 'INNOT', 'camegik', 'Emisael', 'xdd', 'Chesis', 'arfimo', 'GM BON', 'BigMort2', 'Herbs16', 'Morxillita', 'JoshuaAllier', 'Wightslayer', 'kokos71914', 'mike-megamis', 'Roderiston']

@bot.command()
async def morir(ctx):
    """Adds two numbers together."""
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name="Muelto")
    if not role:
        await ctx.send(f"The role 'Muelto' does not exist!")
        return

    for username in names_without_human_role:
        # Find the user by username
        member = discord.utils.get(guild.members, display_name=username)

        if member:
            # Add the role to the user
            await member.add_roles(role)
            await ctx.send(f"Assigned 'Muelto' role to {member.name}.")
        else:
            await ctx.send(f"User '{username}' not found.")


    await ctx.send("todo los usuarios han sido añadidos")

bot.run(secrets.BOT_TOKEN)
