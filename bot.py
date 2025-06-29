import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

# Define intents for your bot
intents = nextcord.Intents.default()
intents.message_content = True  # ✅ Enable message content intent
intents.voice_states = True     # ✅ CRITICAL: Ensure this is present and True for voice/music

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    """
    Event handler that runs when the bot successfully connects to Discord.
    It prints a confirmation message.
    """
    print(f"✅ Logged in as {bot.user}")

# Load all cogs from the 'cogs' directory
for filename in os.listdir("./cogs"):
    # This ensures it loads Python files and skips 'init.py'
    if filename.endswith(".py") and filename != "init.py":
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"✅ Loaded cog: {filename}")
        except Exception as e:
            print(f"❌ Failed to load cog {filename}: {e}")

# Run the bot using the Discord token loaded from your .env file
bot.run(os.getenv("DISCORD_TOKEN"))
