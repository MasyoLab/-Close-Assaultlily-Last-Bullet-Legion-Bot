import discord
from discord.ext import commands
import os
import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN_2']


@bot.event
async def on_ready():
    startTime = datetime.datetime(2021, 1, 20)
    endTime = datetime.datetime.now()
    game = discord.Game('CHARMの妖精', start=startTime, end=endTime)
    await bot.change_presence(status=discord.Status.online, activity=game)


def client_run():
    bot.run(token)


async def async_client_run():
    await bot.start(token)
