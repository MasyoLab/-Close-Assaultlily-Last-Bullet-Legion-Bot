import discord
from discord.ext import commands
import os
import datetime

DIFF_JST_FROM_UTC = 9

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_ready():
    startTime = datetime.datetime(2021, 1, 20)
    nowTime = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
    game = discord.Game(name='Assaultliliy', start=startTime, end=nowTime)
    await bot.change_presence(status=discord.Status.online, activity=game)


def client_run():
    bot.run(token)


async def async_client_run():
    await bot.start(token)
