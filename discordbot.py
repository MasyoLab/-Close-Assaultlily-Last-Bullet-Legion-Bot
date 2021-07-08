import discord
from discord.ext import commands
import os

# 接続に必要なオブジェクトを生成
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
SEND_CHANNEL = os.environ['SEND_CHANNEL']  # 送信用チャンネル
ASSAULTLILY_LOG_CHANNEL = os.environ['ASSAULTLILY_LOG'] # レギオンマッチ ログ

@client.event
# メッセージを受け取った際のイベント
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # 送信用チャンネルかを確認
    if message.channel.id == SEND_CHANNEL:
        # 送信先チャンネルを設定
        target_channel = client.get_channel(ASSAULTLILY_LOG_CHANNEL)
        # 送信用チャンネルから受け取った内容を送信
        await target_channel.send(message.content)

# Botの起動とDiscordサーバーへの接続
client.run(token)