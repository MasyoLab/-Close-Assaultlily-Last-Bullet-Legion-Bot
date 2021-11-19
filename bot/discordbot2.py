import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN_2']
channel1 = os.environ['BOT2_GET_CHANNEL_ID']
channel2 = os.environ['BOT2_POST_CHANNEL_ID']


@bot.event
async def on_ready():
    game = discord.Game(name='CHARMの妖精')
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command()
async def ping1(ctx):
    await ctx.send(channel1)


@bot.command()
async def ping2(ctx):
    await ctx.send(ctx.channel.id)


@bot.command()
async def ping3(ctx: commands.Command):
    await ctx.send(bot.get_all_channels())


@bot.command()
async def ping4(ctx):
    target_channel = bot.get_channel(channel1)
    await ctx.send(target_channel.channel.id)


def client_run():
    bot.run(token)


async def async_client_run():
    await bot.start(token)
