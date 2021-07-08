from discord.ext import commands
import os
import traceback
from boto.s3.connection import S3Connection

# 接続に必要なオブジェクトを生成
bot = commands.Bot(command_prefix='/')

token = S3Connection(os.environ['DISCORD_BOT_TOKEN'])
send_channel = S3Connection(os.environ['SEND_CHANNEL'])  # 送信用チャンネル
assaultlily_log_channel = S3Connection(os.environ['ASSAULTLILY_LOG']) # レギオンマッチ ログ

@bot.event
# メッセージを受け取った際のイベント
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # 送信用チャンネルかを確認
    if message.channel.id == send_channel:
        # 送信先チャンネルを設定
        target_channel = bot.get_channel(assaultlily_log_channel)
        # 送信用チャンネルから受け取った内容を送信
        await target_channel.send(message.content)

# Botの起動とDiscordサーバーへの接続
bot.run(token)