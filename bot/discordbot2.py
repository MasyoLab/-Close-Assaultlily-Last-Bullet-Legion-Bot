import discord
from discord.ext import commands
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN_2']
get_channel_id = os.environ['BOT2_GET_CHANNEL_ID']
post_channel_id = os.environ['BOT2_POST_CHANNEL_ID']


@client.event
async def on_ready():
    game = discord.Game(name='CHARMの妖精')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    await message.channel.send(message.content)


def client_run():
    client.run(token)


async def async_client_run():
    await client.start(token)
