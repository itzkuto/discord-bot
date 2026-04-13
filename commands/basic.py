from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Bot is alive")

    @commands.command()
    async def join(self, ctx):
        print("JOIN COMMAND TRIGGERED")

        if not ctx.author.voice:
            await ctx.send("You must be in a voice channel first.")
            return

        channel = ctx.author.voice.channel

        try:
            if ctx.voice_client:
                await ctx.voice_client.move_to(channel)
            else:
                await channel.connect()

            await ctx.send("Joined voice channel 🎙️")

        except Exception as e:
            print("VOICE ERROR:", e)
            await ctx.send("Failed to join VC ❌")

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Left voice channel 👋")
        else:
            await ctx.send("I'm not in a voice channel.")


async def setup(bot):
    await bot.add_cog(Basic(bot))
