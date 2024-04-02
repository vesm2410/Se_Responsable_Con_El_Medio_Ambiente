import discord, random, os

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Activa el privilegio de ver miembros
intents.members = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Hemos iniciado sesión como {client.user}")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("$help"):
        await message.channel.send("Hola! Este bot puede... \n 1. ($intro) Introducción al tema \n 2. ($tipsCO2) Tips Para Reducir el CO2,  \n 3. ($tipsa) Tips Con Agua \n 4. ($tipse) Tips Con Electricidad ")
    elif message.content.startswith("$intro"):
        await message.channel.send("Hay que mejorar el consumo de recursos naturales, usando los comandos sugeridos en $help se aprenderan unos tips.")
    elif message.content.startswith("$tipsCO2"):
        await message.channel.send("1. Usar el transporte publico puede ayudar a reducir la produccion del CO2 \n 2. Si vas a viajar distancias cortas, ve a pie, es sano para ti y de esa forma te ahorras combustible \n 3. Los autos electricos no son perfectos pero reducen considerablemente tu huella de carbono \n 4.Caminar te mantiene sano y no utiliza combustible fosil \n 5. Viajar en bicicleta es buena forma de ejercitarse y a la vez reducir la produccion de gases")
    elif message.content.startswith("$tipsa"):
        await message.channel.send("1. Toma duchas más breves y cierra las llaves mientras te enjabonas o aplicas champú. \n 2. Aprovecha el agua que al principio sale fría, en lo que se calienta. \n 3. Cierra el grifo mientras te cepillas los dientes o te lavas las manos. \n 4. Lava la ropa en cargas completas. \n \n Utiliza estos tips y ayudaras al medio ambiente!!!")
    elif message.content.startswith("$tipse"):
        await message.channel.send("1. Usa focos ahorradores, iluminan igual que los incandescentes y consumen 75% menos energía. \n 2. Aprovecha la luz natural del día mediante la orientación adecuada de ventanas, y usa colores claros en paredes, techos, pisos y mobiliario. \n 3. Apaga focos y desconecta aparatos.")
#    else:
#        await message.channel.send("a")

client.run("token secreto ¬_¬")
