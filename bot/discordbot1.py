from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


async def on_ready():
    game = bot.Game('Assaultliliyをプレイ中')
    await bot.change_presence(status=bot.Status.online, activity=game)


def client_run():
    bot.run(token)


async def async_client_run():
    await bot.start(token)
