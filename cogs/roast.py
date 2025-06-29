from nextcord.ext import commands
import nextcord
import google.generativeai as genai
import os
import json

ROASTED_FILE = "roasted_messages.json"

class Roast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(
            "gemini-2.0-flash-001",
            generation_config=genai.types.GenerationConfig(
                temperature=0.9,
                max_output_tokens=25
            ),
        )

        # Load roasted message IDs from file
        if os.path.exists(ROASTED_FILE):
            with open(ROASTED_FILE, "r") as f:
                self.roasted_message_ids = set(json.load(f))
        else:
            self.roasted_message_ids = set()

    def save_roasted_ids(self):
        with open(ROASTED_FILE, "w") as f:
            json.dump(list(self.roasted_message_ids), f)

    @nextcord.slash_command(name="roast", description="Roast someone using AI")
    async def roast(self, interaction: nextcord.Interaction, target: nextcord.Member):
        await interaction.response.defer(ephemeral=True)

        # collect last 50 messages from the target in this channel that haven't been roasted
        messages = []
        async for msg in interaction.channel.history(limit=500):
            if msg.author == target and msg.id not in self.roasted_message_ids and msg.content.strip():
                messages.append(msg)
                if len(messages) >= 50:
                    break

        if not messages:
            return await interaction.followup.send(
                f"❌ couldn't find any unroasted messages from {target.mention} in this channel"
            )

        # pick the longest message as most roastable
        target_message = max(messages, key=lambda m: len(m.content))

        # prompt
        prompt = (
            f"you're an edgy teenager who roasts people based only on what they text\n"
            f"here's their message: {target_message.content}\n"
            "make a one-line roast with no punctuation except for commas, no caps and make it short and funny"
        )

        try:
            response = self.model.generate_content(prompt)
            roast_text = response.text.strip()

            # mark as roasted and save to file
            self.roasted_message_ids.add(target_message.id)
            self.save_roasted_ids()

            # reply to that message
            await target_message.reply(
                f"{roast_text}\n\n*roast submitted by {interaction.user.display_name}*"
            )
            await interaction.followup.send("✅ roast sent!")
        except Exception as e:
            await interaction.followup.send(f"❌ Gemini API error: {e}")

def setup(bot):
    bot.add_cog(Roast(bot))
