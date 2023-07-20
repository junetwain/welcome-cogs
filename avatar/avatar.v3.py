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

        url = user.avatar.with_format("png")

        # Get the user's name without discriminator
        username_without_discriminator = user.name

        # Create a custom color with RGB values for #A50903 (deep red)
        custom_color = discord.Color.from_rgb(165, 9, 3)

        embed = Embed(title=f"{username_without_discriminator}'s Avatar", color=custom_color)

        # Set the avatar as the image for the embed to display a bigger image
        embed.set_image(url=url)

        await ctx.send(embed=embed)
