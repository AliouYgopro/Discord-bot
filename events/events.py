from nextcord import Message
from nextcord.ext import commands, tasks
from colorama import Fore, Style
from core import ViewUpdates, Functions, YGOFunctions
import nextcord
from config import config
import asyncio

class Events(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		self.ViewUpdate = ViewUpdates(self.bot)
		self.functions = Functions(self.bot)
		self.ygo_search = YGOFunctions(self.bot)
		
		
		#-------------(tasks start)
		
		self.UpdateCards.start()
		
	#----------------(tasks)
		
	@tasks.loop(hours=3)
	async def UpdateCards(self):
		await self.ygo_search.update_cards()
	
	#----------------(events)
	
	#on_message member
	@commands.Cog.listener()
	async def on_message(self, message: Message):
		
		if message.author.bot:
			return
			
		await self.ygo_search.EventSearch(message=message)
		
	#on_member_join
	@commands.Cog.listener()
	async def on_member_join(self, member):
		if member.bot:
			return
			
		await self.functions.Welcome(user=member, guild=member.guild)
	
	#on_ready
	@commands.Cog.listener()
	async def on_ready(self):
		
		self.functions.Add_View()
		await self.ViewUpdate.Run()
		print(Fore.LIGHTMAGENTA_EX + " • Developed by: " + Fore.LIGHTRED_EX + "𝙔𝙐𝙎𝙄")
		print(Fore.LIGHTCYAN_EX + " • Name: " + Fore.LIGHTRED_EX + f"{self.bot.user.name}")
		print(Fore.LIGHTMAGENTA_EX + " • Bot is: " + Fore.LIGHTGREEN_EX + "Online")
	
		
def setup(bot):
	bot.add_cog(Events(bot))