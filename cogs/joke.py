import random
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, app_commands

class Jokes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.english_jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "What do you call fake spaghetti? An impasta!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "What do you call cheese that isn't yours? Nacho cheese!",
            "Why can’t your nose be 12 inches long? Because then it would be a foot.",
            "How does a penguin build its house? Igloos it together.",
            "I'm reading a book about anti-gravity. It's impossible to put down!",
            "Why don't eggs tell jokes? They'd crack each other up.",
            "How do you organize a space party? You planet.",
            "Why did the bicycle fall over? Because it was two-tired.",
            "Why did the math book look sad? Because it had too many problems.",
            "Why did the cookie go to the hospital? Because it felt crummy.",
            "What did one plate say to the other? Lunch is on me.",
            "Why can't you give Elsa a balloon? Because she will let it go.",
            "What do you call a belt made of watches? A waist of time.",
            "How do cows stay up to date? They read the moos-paper.",
            "Why did the tomato turn red? Because it saw the salad dressing.",
            "What do you call a pile of cats? A meowtain.",
            "What do you call a fish with no eyes? Fsh.",
            "What do you call a can opener that doesn’t work? A can't opener.",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
            "What’s orange and sounds like a parrot? A carrot.",
            "What do you call a dinosaur with an extensive vocabulary? A thesaurus.",
            "Why was the broom late? It swept in.",
            "How does a vampire start a letter? Tomb it may concern.",
            "Why do bees have sticky hair? Because they use honeycombs.",
            "What kind of tree fits in your hand? A palm tree.",
            "What do you call two birds in love? Tweethearts.",
            "Why did the music teacher go to jail? Because she got caught with too many notes.",
            "What did the zero say to the eight? Nice belt!",
            "How do you make holy water? You boil the hell out of it.",
            "Why are frogs so happy? They eat whatever bugs them.",
            "Why did the banker quit his job? He lost interest.",
            "Why did the coffee file a police report? It got mugged.",
            "What do you call an elephant that doesn’t matter? An irrelephant.",
            "Why don’t some couples go to the gym? Because some relationships don’t work out.",
            "What did the grape do when he got stepped on? Nothing but let out a little wine.",
            "Why was the computer cold? It left its Windows open.",
            "What do you call a snowman with a six-pack? An abdominal snowman.",
            "Why did the cow go to outer space? To visit the Milky Way.",
            "Why don’t oysters donate to charity? Because they’re shellfish.",
            "What did the janitor say when he jumped out of the closet? Supplies!",
            "What do you get from a pampered cow? Spoiled milk.",
            "Why do seagulls fly over the sea? Because if they flew over the bay, they’d be bagels.",
            "What kind of music do mummies listen to? Wrap music.",
            "How do you catch a squirrel? Climb a tree and act like a nut.",
            "Why don’t crabs give to charity? Because they’re shellfish."
        ]

        self.spanish_jokes = [
            "¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas.",
            "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
            "¿Cuál es el colmo de Aladdín? Tener mal genio.",
            "¿Cómo se despiden los químicos? Ácido un placer.",
            "¿Qué le dice una iguana a su hermana gemela? ¡Iguanita!",
            "¿Qué hace una computadora en el mar? Nada.",
            "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
            "¿Cómo se llama el campeón de buceo japonés? Tokofondo.",
            "¿Y el subcampeón? Kasitoko.",
            "¿Qué hace una vaca en un terremoto? Leche agitada.",
            "¿Qué le dice un jardinero a otro? ¡Disfrutemos mientras podamos!",
            "¿Cómo se dice pañuelo en japonés? Saka-moko.",
            "¿Qué le dice un pez a otro pez? ¡Nada, nada!",
            "¿Por qué lloraba el libro de matemáticas? Porque tenía muchos problemas.",
            "¿Qué hace un pez? Nada.",
            "¿Por qué está feliz la escoba? Porque ba-rriendo.",
            "¿Cómo se dice pelo sucio en chino? Chin cham pu.",
            "¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro.",
            "¿Qué hace una taza en la escuela? Taza tareas.",
            "¿Por qué los esqueletos no pelean entre ellos? Porque no tienen agallas.",
            "¿Qué hace un perro con un taladro? Taladrando.",
            "¿Por qué el plátano fue al médico? Porque no se pelaba bien.",
            "¿Cómo se llama el campeón de buceo ruso? Ivan Profundo.",
            "¿Qué le dice un gusano a otro gusano? Voy a dar una vuelta a la manzana.",
            "¿Qué hace un león en el gimnasio? ¡Musculión!",
            "¿Qué le dice un techo a otro? Techo de menos.",
            "¿Qué hace una caja hablando con otra? Se cuentan cosas.",
            "¿Por qué el tomate se sonrojó? Porque vio al otro desnudo.",
            "¿Qué hacen dos pollos en una panadería? Pío pío pán.",
            "¿Cómo se dice pañuelo en ruso? Kasitovoski.",
            "¿Cuál es el café más peligroso del mundo? El ex-preso.",
            "¿Por qué no juegan al escondite los árboles? Porque siempre se les ve el tronco.",
            "¿Qué hace un gato en la calle? ¡Miau-vilizando!",
            "¿Por qué los peces no van al cine? Porque ya lo han visto todo.",
            "¿Cómo se dice pañuelo en árabe? Tapasnarís.",
            "¿Qué hace un pato con una pata rota? Cojea.",
            "¿Qué le dice una piedra a otra? La vida es dura.",
            "¿Por qué la escoba está cansada? Porque barre mucho.",
            "¿Qué hace una oreja en una clase de música? Escucha bien.",
            "¿Cómo se dice pelo sucio en coreano? Chin-champú.",
            "¿Qué hace un pez en una biblioteca? Nada entre libros.",
            "¿Cómo se despiden los químicos? Ácido un placer.",
            "¿Qué hace una vaca en un baño? Se baña-muuu.",
            "¿Cuál es el colmo de un electricista? No encontrar su corriente de trabajo.",
            "¿Qué hace una abeja con un martillo? ¡Zumba clavos!",
            "¿Por qué el reloj fue a terapia? Porque tenía problemas de tiempo.",
            "¿Qué hace un globo en el cielo? ¡Nada, solo se infla!",
            "¿Qué le dice el 1 al 10? Para ser como yo, tienes que ser sincero.",
            "¿Qué le dice una bombilla a otra? Me tienes encendida.",
            "¿Cómo se dice pelo sucio en alemán? Shampukaput."
        ]

    @app_commands.command(name="joke", description="Get a random joke in English or Spanish.")
    @app_commands.describe(language="Choose the language of the joke")
    @app_commands.choices(language=[
        app_commands.Choice(name="English", value="english"),
        app_commands.Choice(name="Spanish", value="spanish")
    ])
    async def joke(self, interaction: Interaction, language: app_commands.Choice[str]):
        if language.value == "english":
            joke = random.choice(self.english_jokes)
        else:
            joke = random.choice(self.spanish_jokes)

        await interaction.response.send_message(joke)

    async def cog_load(self):
        self.bot.tree.add_command(self.joke)

def setup(bot: commands.Bot):
    bot.add_cog(Jokes(bot))
