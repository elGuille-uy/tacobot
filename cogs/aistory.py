from nextcord.ext import commands
import nextcord
import google.generativeai as genai
import os

class AIStory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(
            "gemini-2.0-flash-001",
            generation_config=genai.types.GenerationConfig(
                temperature=1.2,
                max_output_tokens=180  # shorter story length
            ),
        )

    @nextcord.slash_command(name="aistory", description="Generate an unhinged short story with AI")
    async def aistory(self, interaction: nextcord.Interaction, prompt: str):
        await interaction.response.defer()

        story_prompt = (
            f"Write a very short, bizarre, unhinged, chaotic third-person story based on this concept: {prompt}. "
            "Do NOT use the name Bartholomew or any other repeated default names. "
            "Use only names or characters mentioned in the prompt if any. "
            "Make it weird, wild, fast-paced, and avoid philosophical or deep themes. "
            "Keep the story fresh, surprising, and end clearly within 180 tokens."
        )

        try:
            response = self.model.generate_content(story_prompt)
            story = response.text.strip()
            await interaction.followup.send(f"🧠 **Story by AI**\n{story}")
        except Exception as e:
            await interaction.followup.send(f"❌ Gemini API error: {e}")

def setup(bot):
    bot.add_cog(AIStory(bot))
