import discord
import os
import requests
import random
import aiohttp
import json
from discord.ext import commands
from settings import *
from definiciones import *
actividad = discord.Activity(type=discord.ActivityType.watching,name="formas de reutilizar basura")
bot = commands.Bot(command_prefix=settings["prefix"], intents= discord.Intents.all(), status=discord.Status.dnd, activity=actividad)
bot.remove_command("help")
async def cambiar_imagen():
    url_imagen = 'https://cope-cdnmed.cope.es/resources/jpg/4/1/1597149701714.jpg'
    async with aiohttp.ClientSession() as session:
        async with session.get(url_imagen) as response:
            if response.status != 200:
                print('No se pudo obtener la imagen.')
                return
            data = await response.read()
    await bot.user.edit(avatar=data)
    print('Imagen cambiada exitosamente.')
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
    await cambiar_imagen()
@bot.event
async def on_disconnect():
    # Verificar si el bot está conectado a un canal de voz y desconectarlo
    for vc in bot.voice_clients:
        await vc.disconnect()
        print(f'Bot desconectado del canal de voz {vc.channel.name}')
@bot.command()
async def consejo(ctx, message: str = None, *, message2: str = None):
    frases = cargar_consejos()
    if message == "+":
        if "consejos" not in frases:
            frases["consejos"] = []  # Si no existe la clave "consejos", inicializa una lista vacía
        if message2 not in frases["consejos"]:  # Asegúrate de que el consejo no esté ya en la lista
            frases["consejos"].append(message2)  # Agrega el nuevo consejo a la lista
            guardar_frases(frases)
            await ctx.send(f'El consejo "{message2}" se ha agregado correctamente.')
            message2 = None
        else:
            await ctx.send(f'El consejo "{message2}" ya existe en la lista.')
    else:
        try:
            consejos = frases.get("consejos", [])  # Obtén la lista de consejos, si no existe, devuelve una lista vacía
            if consejos:
                consejo_elegido = random.choice(consejos)
                await ctx.send(f'Consejo aleatorio:\n{consejo_elegido}')
                
            else:
                await ctx.send('La lista de consejos está vacía.')
        except Exception as e:
            await ctx.send(f'Error al cargar la lista de consejos: {e}')

@bot.command()
async def natural(ctx):
    ruta = "C:\\Users\\crush\\Desktop\\Phyton\\BasuraBot\\images"
    with open(f'{ruta}\\natu{random.randint(1,20)}.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run(settings["TOKEN"])