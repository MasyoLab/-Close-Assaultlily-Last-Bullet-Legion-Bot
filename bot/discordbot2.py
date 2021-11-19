import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN_2']


@bot.event
async def on_ready():
    game = discord.Game(name='CHARMの妖精')
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(
        traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


def client_run():
    bot.run(token)


async def async_client_run():
    await bot.start(token)
