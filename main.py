# type: ignore
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
import aiohttp

load_dotenv()

discord_token = os.getenv("BOT_TOKEN")

intents = nextcord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    if message.content == os.getenv("SECRET"):
        await message.reply(os.getenv("SECRET_RESPONSE"))

@bot.slash_command(name="ping", description="Pings the bot to check its status")
async def ping(interaction: nextcord.Interaction):
    await interaction.response.send_message("ponggy pong :3")

@bot.slash_command(name="three", description="3 2 1")
async def three(interaction: nextcord.Interaction):
    await interaction.response.send_message("3")
    for i in range(2):
        await interaction.channel.send(str(2-i))
        await asyncio.sleep(1)

@bot.slash_command(name="isup", description="Checks if sovietcord is up")
async def sovietcordup(interaction: nextcord.Interaction):
    embed = nextcord.Embed(title="SovietCord Status", description=f"Fetching...", color=0xaeb11f)
    embed.set_footer(text="*sovietcord noises*")
    await interaction.response.send_message(embed=embed)

    async with aiohttp.ClientSession() as session:
        async with session.get('https://discvietrdapp.com/') as response:
            if response.status == 200:
                embed = nextcord.Embed(title="SovietCord Status", description="SovietCord is so up rn", color=0x409217)
            else:
                embed = nextcord.Embed(title="SovietCord Status", description="Something happened, pwease check status", color=0xa80000)
        embed.set_footer(text=f"Status code: {response.status}")

    await interaction.edit_original_message(embed=embed)


bot.run(discord_token)