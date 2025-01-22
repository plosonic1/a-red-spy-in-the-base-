import discord
from discord.ext import commands

# Configura tu token aquí
TOKEN = "MTMzMTcwNDI3MjY5MzIzNTg3Mw.GEjDyn.uhyG1FsaDCXUojTHbQ5V4FzA4MT1UtvOhaDAr0"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="?", intents=intents)

# Información de los personajes
team_info = {
    "scout": {
        "name": "Scout",
        "description": "Un joven rápido con doble salto y actitud arrogante.",
        "image": "https://wiki.teamfortress.com/w/images/thumb/d/d5/ScoutRED.png/250px-ScoutRED.png"
    },
    "soldier": {
        "name": "Soldier",
        "description": "Un patriota obsesionado con disciplina y explosivos.",
        "image": "https://wiki.teamfortress.com/w/images/thumb/1/1b/SoldierRED.png/250px-SoldierRED.png"
    },
    "pyro": {
        "name": "Pyro",
        "description": "Un piromaniaco misterioso envuelto en un traje ignífugo.",
        "image": "https://wiki.teamfortress.com/w/images/thumb/9/9e/PyroRED.png/250px-PyroRED.png"
    },
    "demoman": {
        "name": "Demoman",
        "description": "Un maestro explosivista escocés amante del caos.",
        "image": "https://wiki.teamfortress.com/w/images/thumb/1/1a/DemomanRED.png/250px-DemomanRED.png"
    },
    "heavy": {
        "name": "Heavy",
        "description": "Un gigante con una ametralladora llamada Sasha.",
        "image": "https://wiki.teamfortress.com/w/images/thumb/8/80/HeavyRED.png/250px-HeavyRED.png"
    },
    "engineer": {
        "name": "Engineer",
        "description": "Un genio técnico con un arsenal de dispositivos.",
        "image": "https://wiki.teamfortress.com/w/images/thumb/8/88/EngineerRED.png/250px-EngineerRED.png"
    },
    "medic": {
        "name": "Medic",
        "description": "Un médico loco con una obsesión por experimentos extremos.",
        "image": "https://wiki.teamfortress.com/w/images/thumb/6/6a/MedicRED.png/250px-MedicRED.png"
    },
    "sniper": {
        "name": "Sniper",
        "description": "Un francotirador letal con precisión quirúrgica.",
        "image": "https://wiki.teamfortress.com/w/images/thumb/b/b5/SniperRED.png/250px-SniperRED.png"
    },
    "spy": {
        "name": "Spy",
        "description": "Un maestro del disfraz y el espionaje.",
        "image": "https://wiki.teamfortress.com/w/images/thumb/a/a7/SpyRED.png/250px-SpyRED.png"
    }
}

@bot.event
async def on_ready():
    print(f"{bot.user} está listo para el Meet the Team.")


@bot.command()
async def meet(ctx, *, character: str = ""):
    character = character.lower().replace("_", " ")  # Reemplaza guion bajo por espacio
    if character in team_info:
        info = team_info[character]
        embed = discord.Embed(
            title=f"{info['name']} - Meet the Team",
            description=info['description'],
            color=discord.Color.red()
        )
        embed.set_image(url=info["image"])
        await ctx.send(embed=embed)
    else:
        await ctx.send("No reconozco a ese personaje. Intenta con: scout, soldier, pyro, demoman, heavy, engineer, medic, sniper, spy.")


bot.run("MTMzMTcwNDI3MjY5MzIzNTg3Mw.GEjDyn.uhyG1FsaDCXUojTHbQ5V4FzA4MT1UtvOhaDAr0")
