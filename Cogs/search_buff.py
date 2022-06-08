from discord.ext import commands
from discord import app_commands, Interaction
import requests
from bs4 import BeautifulSoup as bs


class sex(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="버프검색", description="아직 베타기능입니다 완벽하지 않아요.")
    async def unzi(self, interaction: Interaction, search: str) -> None:
        try:
            url = f"https://ktos.tavernofsoul.com/buffs/?q={search}"
            res = requests.get(url)
            html = res.text
            soup = bs(html, 'lxml')
            table = soup.find('table')
            trs = table.find_all('tr')
            for idx, tr in enumerate(trs):
                if idx > 0:
                    tds = tr.find_all('td')
                    ClassID = tds[0].text.strip()
                    ClassName = tds[1].text.strip()
                    Name = tds[2].text.strip()
                    result = f'{ClassID}\n {ClassName}\n {Name}'
                    await interaction.response.send_message(result)
        except:
            await interaction.response.send_message("버프를 못찾았습니다. 버프명을 정확히 입력해주세요")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(sex(bot))
