from nextcord.ext import commands
import nextcord
import random

class TruthOrDare(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.truths = [
            "what's the most embarrassing thing you've ever done",
            "have you ever had a crush on someone here",
            "what's a secret you’ve never told anyone",
            "what’s your weirdest habit",
            "what’s the last thing you searched on your phone",
            "who in this server would you never want to fight",
            "what’s something you pretend to like but secretly hate",
            "if you could delete one memory, what would it be"
        ]

        self.dares = [
            "send a message with your eyes closed",
            "change your nickname to something cringe for 5 minutes",
            "talk like a pirate for the next 3 messages",
            "say the alphabet backwards as fast as you can",
            "send the last picture you saved on your phone",
            "type a message in all caps with no context",
            "send a voice message saying 'i'm not a bot i swear'",
            "ping someone and compliment them in the weirdest way"
        ]

    @nextcord.slash_command(name="truthordare", description="Play Truth or Dare!")
    async def truthordare(
        self,
        interaction: nextcord.Interaction,
        choice: str = nextcord.SlashOption(
            name="choice",
            description="Pick truth or dare",
            choices=["truth", "dare"]
        )
    ):
        await interaction.response.defer()
        if choice == "truth":
            selected = random.choice(self.truths)
            await interaction.followup.send(f"🧠 Truth: {selected}")
        else:
            selected = random.choice(self.dares)
            await interaction.followup.send(f"🔥 Dare: {selected}")

def setup(bot):
    bot.add_cog(TruthOrDare(bot))
