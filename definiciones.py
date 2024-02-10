import json
import os
import discord
def cargar_consejos():
    try:
        ruta = "C:\\Users\\crush\\Desktop\\Phyton\\BasuraBot\\"
        with open(f'{ruta}frases.json', 'r') as f:
            datos = json.load(f)
            # Si existe una clave "consejos", asegúrate de que sea una lista y elimina duplicados
            if "consejos" in datos:
                datos["consejos"] = list(set(datos["consejos"]))
                return datos
            else:
                return {"consejos": []}  # Si no hay consejos en el archivo, devuelve una lista vacía
    except FileNotFoundError:
        return {"consejos": []}  # Si el archivo no existe, devuelve una lista vacía
def guardar_frases(frases):
    try:
        ruta = "C:\\Users\\crush\\Desktop\\Phyton\\BasuraBot\\"
        with open(f'{ruta}frases.json', 'r') as f:
            datos_existentes = json.load(f)
    except FileNotFoundError:
        datos_existentes = {}

    for categoria, lista_consejos in frases.items():
        if categoria in datos_existentes:
            for consejo in lista_consejos:
                if consejo not in datos_existentes[categoria]:
                    datos_existentes[categoria].append(consejo)
        else:
            datos_existentes[categoria] = lista_consejos

    with open(f'{ruta}frases.json', 'w') as f:
        json.dump(datos_existentes, f, indent=4)