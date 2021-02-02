import discord
from discord.ext import commands
import asyncio
import json

with open("token.txt", newline="") as tokenFile:
    TOKEN = tokenFile.read()

bot = commands.Bot(command_prefix='.vcping')
bot.remove_command("help")

@bot.event
async def on_ready():
    print("\nConnected to Discord.\n")
    print(f"Number of connected servers: {len(await bot.fetch_guilds().flatten())}")
    print(f"Ping: {round(bot.latency * 1000, 2)}ms\n")
    activity = discord.Activity(name='@VC Ping', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

@bot.event
async def on_guild_join(guild):
  print(f"Joined guild {guild.name}.")

@bot.event
async def on_guild_remove(guild):
  print(f"Left guild {guild.name}.")

@bot.event
async def on_message(message):
  if bot.user.mentioned_in(message):
    voice = message.author.voice
    if voice:
      channel = voice.channel
      await message.channel.send(f"Pinging {channel.name}: " + " ".join([member.mention for member in channel.members]))
    else:
      await message.channel.send("You are not in a voice channel!")

bot.run(TOKEN)
