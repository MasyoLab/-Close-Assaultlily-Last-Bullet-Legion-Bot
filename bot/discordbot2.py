import discord
from datetime import datetime
from discord.ext import tasks
import os

# 接続に必要なオブジェクトを生成
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN_2']
get_channel = os.environ['BOT2_GET_CHANNEL_ID']
post_channel = os.environ['BOT2_POST_CHANNEL_ID']


@client.event
async def on_ready():
    game = discord.Game(name='CHARMの妖精')
    await client.change_presence(status=discord.Status.online, activity=game)


def client_run():
    client.run(token)


async def async_client_run():
    await client.start(token)


@client.event
# メッセージを受け取った際のイベント
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # 送信用チャンネルかを確認
    if message.channel.id == get_channel:
        # 送信先チャンネルを設定
        target_channel = client.get_channel(post_channel)
        # 送信用チャンネルから受け取った内容を送信
        await target_channel.send(message.content)
