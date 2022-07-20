from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random


class Randomjpg(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="짤")
    async def randjpg(self, ctx):
        res = requests.get('http://rangings.com/img')
        soup = BeautifulSoup(res.content, 'html.parser')
        links = soup.find_all('a')
        cell_line = []
        for i in links:
            href = i.attrs['href']
            cell_line.append(href)

        baseurl = 'http://rangings.com/img/'
        sumurl = baseurl + random.choice(cell_line)
        await ctx.send(sumurl)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Randomjpg(bot)
    )
