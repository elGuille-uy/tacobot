from nextcord.ext import commands
import nextcord
import google.generativeai as genai
import os

class AskAI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(
            "gemini-2.0-flash-001",
            generation_config=genai.types.GenerationConfig(
                temperature=0.85,
                max_output_tokens=30
            )
        )

    @nextcord.slash_command(name="askai", description="Ask AI a question with casual short answers")
    async def askai(self, interaction: nextcord.Interaction, question: str):
        await interaction.response.defer()

        prompt = (
            "you are a chill 15 year old who talks casually and swears sometimes but not too much "
            "be funny edgy natural reply like a normal teen no caps no punctuation answer very shortly "
            "like one or two sentences dry and casual no extra fluff here is the question: "
            + question
        )

        try:
            response = self.model.generate_content(prompt)
            answer = response.text.strip()
            sent_msg = await interaction.followup.send(f"**Q:** {question}\n**A:** {answer}")
            # save message id for conversation context
            self.last_bot_message_id = sent_msg.id
        except Exception as e:
            await interaction.followup.send(f"❌ Gemini API error: {e}")

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        # Ignore bot's own messages
        if message.author.bot:
            return

        # Check if this message is a reply to the bot's last AI reply
        if message.reference and message.reference.message_id == getattr(self, "last_bot_message_id", None):
            try:
                # fetch the replied message content (the bot's last reply)
                replied_msg = await message.channel.fetch_message(message.reference.message_id)
            except Exception:
                replied_msg = None

            if replied_msg and replied_msg.author == self.bot.user:
                # Build prompt using the bot's last message + user's new reply
                context = replied_msg.content
                user_msg = message.content

                prompt = (
                    "you are a chill 15 year old who talks casually and swears sometimes but not too much "
                    "be funny edgy natural reply like a normal teen no caps no punctuation answer very shortly "
                    "like one or two sentences dry and casual no extra fluff here is the previous message: "
                    f"{context}\n and now answer this question: {user_msg}"
                )

                try:
                    response = self.model.generate_content(prompt)
                    answer = response.text.strip()
                    sent_msg = await message.channel.send(f"**Q:** {user_msg}\n**A:** {answer}", reference=message)
                    self.last_bot_message_id = sent_msg.id
                except Exception as e:
                    await message.channel.send(f"❌ Gemini API error: {e}", reference=message)

def setup(bot):
    bot.add_cog(AskAI(bot))
