from nextcord.ext import commands
import nextcord
import random

class CoinFlip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_streaks = {}

    @nextcord.slash_command(name="coinflip", description="Flip a coin")
    async def coinflip(self, interaction: nextcord.Interaction):
        user_id = interaction.user.id
        result = random.choice(["Heads", "Tails"])

        streak_data = self.user_streaks.get(user_id)

        if streak_data:
            if streak_data["last_result"] == result:
                # Same result as last time, increment streak
                streak_data["streak"] += 1
                streak = streak_data["streak"]
                await interaction.response.send_message(
                    f"🪙 the coin landed on **{result}**.\nyou have a **{streak}** streak"
                )
            else:
                # Streak lost
                self.user_streaks[user_id] = {"last_result": result, "streak": 1}
                await interaction.response.send_message(
                    f"🪙 The coin landed on **{result}**.\nyou just lost your streak"
                )
        else:
            # First time flipping
            self.user_streaks[user_id] = {"last_result": result, "streak": 1}
            await interaction.response.send_message(f"🪙 the coin landed on **{result}**")

def setup(bot):
    bot.add_cog(CoinFlip(bot))
