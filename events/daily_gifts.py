from nextcord import Message
from nextcord.ext import commands, tasks
from colorama import Fore, Style
from core import ViewUpdates, Functions, YGOFunctions
import nextcord
from config import config
import asyncio

class DailyGifts(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		self.functions = Functions(self.bot)
		
		self.daily.start()
	
	@tasks.loop(hours=24)
	async def daily(self):
		await self.functions.Dailygift()

		
		
def setup(bot):
	bot.add_cog(DailyGifts(bot))