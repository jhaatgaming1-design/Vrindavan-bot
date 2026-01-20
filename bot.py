
import discord
from discord.ext import commands
from config import TOKEN, OWNER_IDS, DEFAULT_PREFIX

intents = discord.Intents.all()

def get_prefix(bot, message):
    if message.author.id in OWNER_IDS:
        return ["", DEFAULT_PREFIX]
    return [DEFAULT_PREFIX]

bot = commands.Bot(command_prefix=get_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Vrindavan Bot Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🌸")

def start_bot():
    bot.run(TOKEN)
