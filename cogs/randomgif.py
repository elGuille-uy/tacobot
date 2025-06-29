from nextcord.ext import commands
import nextcord
import aiohttp

GIPHY_API_KEY = "GzrHgB52R6ZVTFBz90w60hGRO4No6Uoi"  # Replace with your Giphy API key

class RandomGif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="randomgif", description="Get a random gif from Giphy")
    async def randomgif(self, interaction: nextcord.Interaction):
        await interaction.response.defer()  # Give more time for API response

        url = f"https://api.giphy.com/v1/gifs/random?api_key={GIPHY_API_KEY}&rating=pg-13"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    await interaction.followup.send("❌ Failed to fetch GIF from Giphy.")
                    return

                data = await resp.json()
                gif_url = data.get("data", {}).get("images", {}).get("original", {}).get("url")

                if not gif_url:
                    await interaction.followup.send("❌ Couldn't find a GIF this time, try again!")
                    return

                await interaction.followup.send(gif_url)

def setup(bot):
    bot.add_cog(RandomGif(bot))
