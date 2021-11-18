import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN_2']
get_channel_id = os.environ['BOT2_GET_CHANNEL_ID']
post_channel_id = os.environ['BOT2_POST_CHANNEL_ID']


@bot.event
async def on_ready():
    game = discord.Game(name='CHARMの妖精')
    await bot.change_presence(status=discord.Status.online, activity=game)


# @bot.command()
# async def on_message(message: discord.Message):
#    bot.get_channel
#    if message.channel == get_channel_id:
#        target_channel = bot.get_channel(post_channel_id)
#        await target_channel.send(message.content)
@bot.command(pass_context=True)
async def xsend(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    channel = bot.get_channel(post_channel_id)
    if channel:
        await bot.send_message(channel, message)


def client_run():
    bot.run(token)


async def async_client_run():
    await bot.start(token)
