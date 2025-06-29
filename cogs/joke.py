import random
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Jokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.english_jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why did the math book look sad? Because it had too many problems.",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "What do you call fake spaghetti? An impasta!",
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "Why can’t your nose be 12 inches long? Because then it would be a foot.",
            "What do you call cheese that isn't yours? Nacho cheese.",
            "I used to be addicted to the hokey pokey, but then I turned myself around.",
            "Why did the bicycle fall over? It was two-tired!",
            "Why don’t eggs tell jokes? They’d crack each other up.",
            "What’s orange and sounds like a parrot? A carrot.",
            "How does a penguin build its house? Igloos it together.",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
            "Why can’t you hear a pterodactyl go to the bathroom? Because the P is silent.",
            "Why was Cinderella so bad at soccer? She always ran away from the ball.",
            "How do cows stay up to date? They read the moos-paper.",
            "What do you get from a pampered cow? Spoiled milk.",
            "Why did the chicken join a band? Because it had the drumsticks.",
            "What do you call a pile of cats? A meow-tain.",
            "I made a pencil with two erasers. It was pointless.",
            "Why was the computer cold? It left its Windows open.",
            "Why did the coffee file a police report? It got mugged.",
            "What do you call a singing computer? A-Dell.",
            "What did the ocean say to the beach? Nothing, it just waved.",
            "Why don’t programmers like nature? It has too many bugs.",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "How do you organize a space party? You planet.",
            "Why was the math teacher suspicious of prime numbers? They were always odd.",
            "How do you make a tissue dance? Put a little boogie in it.",
            "What did one wall say to the other? I’ll meet you at the corner.",
            "Why did the cookie go to the hospital? Because it felt crummy.",
            "Why did the man put his money in the freezer? He wanted cold hard cash.",
            "I told my computer I needed a break, and it said no problem — it needed one too.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "What did the grape do when he got stepped on? Nothing but let out a little wine.",
            "I once got fired from a canned juice company. Apparently, I couldn’t concentrate.",
            "Why are frogs so happy? Because they eat whatever bugs them.",
            "Why don't some couples go to the gym? Because some relationships don't work out.",
            "Why did the computer go to therapy? It had too many tabs open.",
            "Why are elevator jokes so classic? They work on many levels.",
            "Why did Elsa not hold the balloon? Because she let it go.",
            "Why do bees have sticky hair? Because they use honeycombs.",
            "Why did the belt get arrested? For holding up the pants!",
            "Why did the picture go to jail? Because it was framed.",
            "Why do bakers always feel exhausted? Because they knead the dough.",
            "Why can't bicycles stand up by themselves? They're two-tired!",
            "Why did the stadium get hot after the game? All the fans left.",
            "Why was the broom late? It swept in."
        ]

        self.spanish_jokes = [
            "¿Por qué el libro de matemáticas estaba triste? Porque tenía muchos problemas.",
            "¿Qué le dice una iguana a su hermana gemela? ¡Iguanita!",
            "¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro.",
            "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
            "¿Cómo se dice pañuelo en japonés? Saka-moko.",
            "¿Qué le dice un gusano a otro gusano? Voy a dar una vuelta a la manzana.",
            "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
            "¿Qué le dice un pez a otro pez? ¡Nada, nada!",
            "¿Por qué se cayó el libro de historia? Porque estaba en el pasado.",
            "¿Qué hace una vaca cuando sale el sol? Sombra.",
            "¿Por qué lloraba el tomate? Porque vio al otro ser aplastado.",
            "¿Qué le dijo un plátano a una gelatina? ¡Todavía no tiembles!",
            "¿Por qué no juegan a las escondidas los fantasmas? Porque siempre los descubren.",
            "¿Cómo se despiden los químicos? Ácido un placer.",
            "¿Qué le dice un semáforo a otro? No me mires, me estoy cambiando.",
            "¿Qué le dijo la luna al sol? ¡Tanto tiempo sin vernos!",
            "¿Qué hace una persona con un sobre en la oreja? Escuchando música de sello.",
            "¿Por qué los esqueletos no pelean entre ellos? Porque no tienen agallas.",
            "¿Cuál es el café más peligroso del mundo? El ex-preso.",
            "¿Qué hace un pez? ¡Nada!",
            "¿Qué le dice un jardinero a otro? ¡Disfrutemos mientras podamos!",
            "¿Por qué los pájaros no usan WhatsApp? Porque ya tienen piu-piu.",
            "¿Qué hace una hormiga en el cine? Ve una película de insectos.",
            "¿Cómo se llama el campeón de buceo japonés? Tokofondo.",
            "¿Y el subcampeón? Kasitoko.",
            "¿Qué le dice una cebolla a otra? ¡Eres la única que me hace llorar!",
            "¿Qué hace un perro con un taladro? Taladrando.",
            "¿Qué hace una cuchara en la calle? ¡Sopla!",
            "¿Por qué la escoba está feliz? Porque ba-rriendo.",
            "¿Qué le dice un techo a otro techo? Techo de menos.",
            "¿Cómo se llama el campeón de buceo alemán? Hundido.",
            "¿Cuál es el colmo de Aladdín? Tener mal genio.",
            "¿Por qué no juega bien el equipo de las focas? Porque siempre hacen ¡ooohh!",
            "¿Cuál es el colmo de un electricista? No tener corriente.",
            "¿Qué le dijo el uno al diez? Para ser como yo, tienes que ser sincero.",
            "¿Qué hace un gato en la computadora? Busca en Google.",
            "¿Por qué los esqueletos no mienten? Porque se les ve el hueso.",
            "¿Cómo se llama el pez más divertido? El pez payaso.",
            "¿Por qué los libros no pueden hablar? Porque están escritos.",
            "¿Qué hace un elefante en una fábrica de helados? ¡Mucho frío!",
            "¿Qué hace un reloj en el gimnasio? ¡Marca el tiempo!",
            "¿Cuál es el colmo de un panadero? Tener una hija que se llame Magdalena.",
            "¿Qué hace una servilleta en la escuela? Toma apu-notas.",
            "¿Por qué el pasto no tiene amigos? Porque siempre lo pisan.",
            "¿Qué hace un pato con una pata rota? ¡Cojea!",
            "¿Por qué el sol no va a la escuela? Porque ya tiene muchos grados.",
            "¿Qué le dice una taza a otra taza? ¡Tanto tiempo sin verte!",
            "¿Qué hace un loco en una biblioteca? Busca el libro de cómo escapar.",
            "¿Por qué lloraba la escoba? Porque la habían dejado en el rincón.",
            "¿Por qué la luna se fue triste? Porque nadie la miró esa noche."
        ]

    @commands.slash_command(name="joke", description="Get a random joke in English or Spanish.")
    async def joke(
        self,
        interaction: Interaction,
        language: str = SlashOption(
            name="language",
            description="Choose a language",
            choices=["english", "spanish"]
        )
    ):
        jokes = self.english_jokes if language == "english" else self.spanish_jokes
        await interaction.response.send_message(random.choice(jokes))

def setup(bot):
    bot.add_cog(Jokes(bot))
