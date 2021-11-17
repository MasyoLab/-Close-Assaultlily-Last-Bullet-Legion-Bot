import bot  # folder import
import asyncio


def main():
    loop = asyncio.get_event_loop()

    loop.create_task(bot.discordbot1.async_client_run())
    loop.create_task(bot.discordbot2.async_client_run())

    loop.run_forever()
    # loop.close()


main()
