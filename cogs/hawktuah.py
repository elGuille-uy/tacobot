from nextcord.ext import commands
import nextcord

class PingResponse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author.bot:
            return

        if "hawk" in message.content.lower():
            await message.reply("tuah")

        await self.bot.process_commands(message)  # keeps slash commands working

def setup(bot):
    bot.add_cog(PingResponse(bot))
