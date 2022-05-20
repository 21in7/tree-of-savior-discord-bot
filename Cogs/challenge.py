#모듈 불러오기
import discord
from discord import File
from discord import app_commands
from discord.ext import commands
import datetime
import openpyxl
from discord import Embed
from discord import File
from discord.ui import Button, View

#엑셀 파일 불러오기
wb = openpyxl.load_workbook('challenge.xlsx')
#불러온 엑셀에서 시트 
load_ws = wb['Sheet1']


class challenge(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="메뉴")
    async def challage(self, interaction: discord.Interaction) -> None:
        #지금 날짜 불러오기
        d = datetime.datetime.now()
        #불러올 내용 지정
        str_now = str(d.strftime("%y-%m-%d\n"))
        # 홀수달 짝수달 구분
        if d.month % 2 == 0:
            #짝수달 이면
            col = 2
            send_message = ((load_ws.cell(d.day, col).value))
            wb.close()
        else:
            #홀수달 이면
            col = 1
            send_message = ((load_ws.cell(d.day, col).value))
            wb.close()
        today_embed = Embed(title="오늘의 챌린지",
                            description=str_now + send_message)
        today_file = File(f"./{col}/{d.day}.jpg", filename="image.jpg")
        today_embed.set_image(url="attachment://image.jpg")
        today_embed.set_footer(
            text="루틴표 제공 : 튼튼 한입할게요 \n맵 파일 제공 : 튼튼 한입할게요 \n봇 문의 : 병아리 기현")
        #내일 날짜 구하기
        tomorrow = d + datetime.timedelta(days=1)
        #'일'만 불러오기
        strftime_tomorrow = int(tomorrow.strftime("%d"))
        #불러올 내용 수정
        str_tomorrow = str(tomorrow.strftime("%y-%m-%d\n"))
        #홀수달 짝수달 구분
        if d.month % 2 == 0:
            #짝수달 이면
            co = 2
            to_challange = ((load_ws.cell(strftime_tomorrow, co).value))
            wb.close()
        else:
            #홀수달 이면
            co = 1
            to_challange = ((load_ws.cell(strftime_tomorrow, co).value))
            wb.close()
        tomorrow_embed = Embed(title="내일의 챌린지",
                               description=str(str_tomorrow) + to_challange)
        tomorrow_file = File(
            f"./{co}/{strftime_tomorrow}.jpg", filename="image.jpg")
        tomorrow_embed.set_image(url="attachment://image.jpg")
        tomorrow_embed.set_footer(
            text="루틴표 제공 : 튼튼 한입할게요 \n맵 파일 제공 : 튼튼 한입할게요 \n봇 문의 : 병아리 기현")
        #
        today = Button(label="오늘의 챌", style=discord.ButtonStyle.green)
        tomorrow = Button(label="내일의 챌", style=discord.ButtonStyle.primary)
        burning = Button(label="5월 버닝", style=discord.ButtonStyle.danger)
        tjdanf = Button(label="면류관", style=discord.ButtonStyle.gray)
        tavern = Button(label="tavernofsoul", style=discord.ButtonStyle.link,
                        url="https://ktos.tavernofsoul.com/")
        #오늘의 챌
        async def today_callback(interaction: discord.Interaction):
            await interaction.response.send_message(file=today_file, embed=today_embed)
        #내일의 챌
        async def tommorow_callback(interaction: discord.Interaction):
            await interaction.response.send_message(file=tomorrow_file, embed=tomorrow_embed)
        #버닝
        async def burning_callback(interaction: discord.Interaction):
            await interaction.response.send_message(file=File("./img/unknown.png"))
        #면류관
        async def tjdanf_callback(interaction: discord.Interaction):
            await interaction.response.send_message(file=File("./img/db28631695a79b9e.jpg"))

        
        #오늘의 챌 콜백
        today.callback = today_callback
        #내일의 챌 콜백
        tomorrow.callback = tommorow_callback
        #버닝 콜백
        burning.callback = burning_callback
        #면류관 
        tjdanf.callback = tjdanf_callback
        view = View()
        view.add_item(today)
        view.add_item(tomorrow)
        view.add_item(burning)
        view.add_item(tjdanf)
        view.add_item(tavern)
        await interaction.response.send_message("메뉴를 선택해주세요", view=view)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        challenge(bot)
    )
