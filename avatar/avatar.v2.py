import discord
from discord import Embed
from redbot.core import commands

class Avatar(commands.Cog):
    """Get user's avatar URL."""

    @commands.command()
    async def avatar(self, ctx, *, user: discord.Member=None):
        """Returns user avatar URL.

        User argument can be user mention, nickname, username, user ID.
        Default to yourself when no argument is supplied.
        """
        author = ctx.author

        if not user:
            user = author

        url = user.avatar.with_static_format("png")

        embed = Embed(title=f"{user}'s Avatar", description=f"[Avatar URL]({url})", color=discord.Color.blurple())

        # Set the avatar as the thumbnail for the embed (optional)
        embed.set_thumbnail(url=url)

        await ctx.send(embed=embed)
