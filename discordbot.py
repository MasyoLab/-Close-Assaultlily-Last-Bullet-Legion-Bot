from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/')
bot_token = os.environ['DISCORD_BOT_TOKEN']

# レギオンマッチ専用
legion_match_log_input = os.environ['LEGION_MATCH_LOG_INPUT']
legion_match_log_output = os.environ['LEGION_MATCH_LOG_OUTPUT']


@bot.event
# メッセージを受け取った際のイベント
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # チャンネルIDで送信先を決める

    # レギオンマッチ専用
    if message.channel.id == legion_match_log_input:
        # 送信先チャンネルを設定
        target_channel = bot.get_channel(legion_match_log_output)
        if target_channel:
            # 送信用チャンネルから受け取った内容を送信
            await bot.send_message(target_channel, message.content)

bot.run(bot_token)
