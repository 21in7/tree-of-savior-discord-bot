import asyncio
import discord
from discord.ext import commands
import bot_token
import logging
import logging.handlers
import os

#로그 파일 갯수랑 용량 지정
LOG_MAX_SIZE = 1024*1024*10
LOG_FILE_CNT = 100

#로그 저장
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(
    filename='./logs/bot.log', encoding='utf-8', mode='w', maxBytes=LOG_MAX_SIZE, backupCount=LOG_FILE_CNT)
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=discord.Intents.all(),
            sync_commands=True,
            application_id=input your application id
        )
        self.initial_extension = [
            "Cogs.challenge"
        ]

    async def setup_hook(self):
        for ext in self.initial_extension:
            await self.load_extension(ext)
        await bot.tree.sync()

    async def on_ready(self):
        print("다음으로 로그인 합니다 : ")
        print(self.user.name)
        print(self.user.id)
        print("=============")
        game = discord.Game("Tree Of Savior 🌳")
        await self.change_presence(status=discord.Status.online, activity=game)


bot = MyBot()
bot.remove_command("help")
bot.run()
