import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/')

token = os.environ['DISCORD_BOT_TOKEN_2']
get_channel = os.environ['BOT2_GET_CHANNEL_ID']
post_channel = os.environ['BOT2_POST_CHANNEL_ID']


@bot.event
async def on_ready():
    game = discord.Game(name='CHARMの妖精')
    await bot.change_presence(status=discord.Status.online, activity=game)


def client_run():
    bot.run(token)


async def async_client_run():
    await bot.start(token)


@bot.event
# メッセージを受け取った際のイベント
async def on_message(message: discord.Message):
    # 送信用チャンネルかを確認
    if message.channel.id == get_channel:

        guild: discord.Guild = message.guild()

        # 送信先チャンネルを設定
        target_channel: discord.guild.TextChannel = guild.get_channel(
            post_channel)
        # 送信用チャンネルから受け取った内容を送信
        await target_channel.send(message.content)
