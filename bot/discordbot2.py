import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN_2']


@bot.event
async def on_ready():
    game = discord.Game('CHARMの妖精')
    await bot.change_presence(status=discord.Status.online, activity=game)


def client_run():
    bot.run(token)


async def async_client_run():
    await bot.start(token)
