from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN_2']


def client_run():
    bot.run(token)


async def async_client_run():
    await bot.start(token)
