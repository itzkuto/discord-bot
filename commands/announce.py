import discord
from discord.ext import commands
import config

class Announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, *, message):

        channel = self.bot.get_channel(config.ANNOUNCE_CHANNEL_ID)

        if channel:
            embed = discord.Embed(
                title="📢 SERVER ANNOUNCEMENT",
                description=message,
                color=discord.Color.blue()
            )
            await channel.send(embed=embed)

        await ctx.message.delete()


async def setup(bot):
    await bot.add_cog(Announce(bot))
