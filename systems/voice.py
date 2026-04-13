from discord.ext import tasks
import config
import asyncio

async def start_voice_system(bot):

    async def join_voice():
        channel = bot.get_channel(config.VOICE_CHANNEL_ID)

        if channel:
            if not bot.voice_clients:
                await channel.connect()

    @tasks.loop(seconds=30)
    async def keep_voice_alive():
        channel = bot.get_channel(config.VOICE_CHANNEL_ID)

        if channel:
            if not bot.voice_clients:
                await channel.connect()
            else:
                vc = bot.voice_clients[0]
                if vc.channel.id != config.VOICE_CHANNEL_ID:
                    await vc.move_to(channel)

    await join_voice()

    keep_voice_alive.start()
