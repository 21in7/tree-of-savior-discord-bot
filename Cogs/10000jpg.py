from bs4 import BeautifulSoup
import urllib.request
from discord.ext import commands


class Jpg10000(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="랜덤")
    async def randomjpg(self, ctx):
        base_url = "http://10000img.com/"
        url = "http://10000img.com/ran.php"

        html = urllib.request.urlopen(url)
        source = html.read()
        soup = BeautifulSoup(source, "html.parser")

        img = soup.find("img")
        img_src = img.get("src")
        img_url = base_url + img_src
        img_name = img_src.replace("/", "")
        await ctx.send(img_url)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Jpg10000(bot)
    )
