import os
import discord
from discord.ext import commands
import config
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is online")

    await bot.change_presence(
        activity=discord.Game(name="Managing the server")
    )

    # start voice system
    from systems.voice import start_voice_system
    await start_voice_system(bot)


async def load_commands():
    await bot.load_extension("commands.basic")
    await bot.load_extension("commands.announce")


async def main():
    async with bot:
        await load_commands()
        await bot.start(os.environ.get('TOKEN'))


asyncio.run(main())
