from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')

token = os.environ['DISCORD_BOT_TOKEN']
send_channel = os.environ['SEND_CHANNEL']
assaultlily_log_channel = os.environ['ASSAULTLILY_LOG']

@bot.event
async def on_message(message):

    if message.author.bot:
        return

    if message.channel.id == send_channel:
        target_channel = bot.get_channel(assaultlily_log_channel)
        await target_channel.send(message.content)

bot.run(token)