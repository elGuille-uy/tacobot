from nextcord.ext import commands
import nextcord
import random

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="dice", description="Roll the dice and get a random number!")
    async def dice(
        self,
        interaction: nextcord.Interaction,
        sides: int = nextcord.SlashOption(
            description="The number of sides on the die.",
            default=6,
            min_value=2,
            max_value=100
        )
    ):
        result = random.randint(1, sides)
        await interaction.response.send_message(f":game_die: You rolled a {result} on a {sides}-sided dice!")

def setup(bot):
    bot.add_cog(Dice(bot))
