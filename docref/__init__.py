"""DocRef - Search for references on documentation webpages generated by Sphinx."""
import asyncio

from redbot.core.bot import Red

from .docref import DocRef
from .errors import AlreadyUpToDate  # noqa: F401
from .types import NodeRef  # noqa: F401


async def setup(bot: Red):
    cog = DocRef()
    if asyncio.iscoroutinefunction(bot.add_cog):
        await bot.add_cog(cog)
    else:
        bot.add_cog(cog)
