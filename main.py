import nextcord
from nextcord.ext import commands, tasks
import os
from core import load_extensions, unload_commands, reload_commands, load_commands
from config import config
import asyncio
from keep_alive import keep_alive

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config["prefix"]), intents=nextcord.Intents.all(), case_insensitive=True, strip_after_prefix=True, owner_ids=config["owners"])



@bot.event
async def on_ready():
	
	await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=config["name"]))



@bot.command(name="unload")
@commands.is_owner()
async def Unload_commands(ctx):
	await unload_commands(ctx=ctx, bot=bot)

@bot.command(name="load")
@commands.is_owner()
async def Load_commands(ctx):
	await load_commands(ctx=ctx, bot=bot)
	
@bot.command(name="reload")
@commands.is_owner()
async def Reload_commands(ctx):
	await reload_commands(ctx=ctx, bot=bot)



if __name__ == "__main__":
	load_extensions(bot)
	try:
		bot.run(os.getenv("TOKEN"))
	except AttributeError as Error:
		print(Error)