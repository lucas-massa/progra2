import random
from Constantes import *
import pygame
import os
import json
import datetime
import csv

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

#GENERAL
def crear_elemento_juego(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int) -> dict:
    """Se encarga de crear un elemento en el juego guardando su superficie (textura) y su rectangulo (comportamiento) 

    Args:
        textura (str): Tiene que ser una ruta ya sea relativa o absoluta
        ancho (int): En pixeles el ancho de ese elemento
        alto (int): En pixeles el alto de ese elemento
        pos_x (int): Donde se va a ubicar en el eje x
        pos_y (int): Donde se va a ubicar en el eje y

    Returns:
        dict: El diccionario con el elemento creado
    """
    elemento_juego = {}
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura),(ancho,alto))
    elemento_juego["rectangulo"] = pygame.Rect(pos_x,pos_y,ancho,alto)
    
    return elemento_juego

def crear_lista_respuestas(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int):
    lista_respuestas = []

    for i in range(4):
        respuesta = crear_elemento_juego(textura,ancho,alto,pos_x,pos_y)
        lista_respuestas.append(respuesta)
        pos_y += 80    
        
    return lista_respuestas

def crear_botones_menu() -> list:
    lista_botones = []
    pos_x = 125
    pos_y = 115

    for i in range(4):
        boton = crear_elemento_juego("textura_respuesta.jpg",ANCHO_BOTON,ALTO_BOTON,pos_x,pos_y)
        pos_y += 80
        lista_botones.append(boton)
    
    return lista_botones

def limpiar_superficie(elemento_juego:dict,textura:str,ancho:int,alto:int):
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura),(ancho,alto))

#GENERAL (Tanto en pygame, como en el juego en consola)
def verificar_respuesta(datos_juego: dict, pregunta_actual: dict, respuesta: int) -> bool:
    if pregunta_actual["respuesta_correcta"] == respuesta:
        puntos = PUNTUACION_ACIERTO

        if datos_juego.get("doble_puntaje"):
            puntos *= 2
            datos_juego["doble_puntaje"] = False  # Se consume al usarlo

        datos_juego["puntuacion"] += puntos
        datos_juego["conteo_correctas"] += 1

        if datos_juego["conteo_correctas"] == 5:
            datos_juego["vidas"] += 2
            datos_juego["tiempo_restante"] += 5
            datos_juego["conteo_correctas"] = 0

        retorno = True

    else:
        datos_juego["puntuacion"] -= PUNTUACION_ERROR
        datos_juego["vidas"] -= 1
        datos_juego["conteo_correctas"] = 0
        retorno = False

    return retorno


#GENERAL (Tanto en pygame, como en el juego en consola)
def reiniciar_estadisticas(datos_juego:dict):
    datos_juego["vidas"] = CANTIDAD_VIDAS
    datos_juego["puntuacion"] = 0
    datos_juego["nombre"] = ""
    datos_juego["tiempo_restante"] = TIEMPO_JUEGO
    datos_juego["conteo_correctas"] = 0

def pasar_pregunta(lista_preguntas:list,indice:int,cuadro_pregunta:dict,lista_respuestas:list) -> dict:
    pregunta_actual = lista_preguntas[indice]
    limpiar_superficie(cuadro_pregunta,"textura_pregunta.jpg",ANCHO_PREGUNTA,ALTO_PREGUNTA)
    for i in range(len(lista_respuestas)):
        limpiar_superficie(lista_respuestas[i],"textura_respuesta.jpg",ANCHO_BOTON,ALTO_BOTON)
    
    return pregunta_actual

#GENERAL (PUEDE SERVIRME EN PYGAME)
def mezclar_lista(lista_preguntas:list) -> None:
    random.shuffle(lista_preguntas)

#ESPECIFICA 
def crear_diccionario_alumno(linea: str, separador: str = ",") -> dict:
    linea = linea.replace("\n", "")
    lista_datos = linea.split(separador)

    alumno = {
        "pregunta": lista_datos[0],
        "respuesta_1": lista_datos[1],
        "respuesta_2": lista_datos[2],
        "respuesta_3": lista_datos[3],
        "respuesta_4": lista_datos[4],
        "respuesta_correcta": int(lista_datos[5]),
        "veces_preguntada": int(lista_datos[6]),
        "aciertos": int(lista_datos[7]),
        "fallos": int(lista_datos[8])
    }

    return alumno

def leer_csv_alumnos(nombre_archivo:str,lista_alumnos:list,separador:str = ",") -> bool:
    if os.path.exists(nombre_archivo) == True:
        with open(nombre_archivo,"r",encoding="utf-8") as archivo:
            #Falsa lectura para evitar la cabecera
            archivo.readline()
            #Recorrer todo el archivo e ir creando un diccionario por cada linea
            for linea in archivo:
                diccionario_alumno = crear_diccionario_alumno(linea,separador)
                lista_alumnos.append(diccionario_alumno)
        retorno = True
    else:
        retorno = False
    
    return retorno

def guardar_ranking(nombre, puntuacion, archivo="ranking.json"):

    fila = [nombre, puntuacion, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    # Si el archivo existe, lo leo y agrego la fila
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            matriz = json.load(f)
    else:
        matriz = [["nombre", "score", "fecha"]]  # Cabecera

    matriz.append(fila)
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(matriz, f, ensure_ascii=False, indent=4)

def obtener_top_10(path_json:str) -> list:
    """
    Devuelve el top 10 del ranking almacenado como matriz (lista de listas).
    """
    try:
        with open(path_json, "r", encoding="utf-8") as archivo:
            matriz = json.load(archivo)

        datos_ordenados = sorted(matriz, key=lambda x: int(x[1]), reverse=True)
        top_10 = datos_ordenados[:10]
        return top_10
    except Exception as e:
        print(f"Error leyendo el ranking: {e}")
        return []
    
def mostrar_top_10(pantalla, lista_top_10, pos_inicial, font, color=pygame.Color('black')):
    y = pos_inicial[1]
    mostrar_texto(pantalla, "TOP 10 PROMEDIOS", (pos_inicial[0], y), font, color)
    y += 40
    for i, jugador in enumerate(lista_top_10, 1):
        nombre = jugador.get("nombre", "Sin nombre")
        score = jugador.get("Score", jugador.get("score", 0))
        texto = f"{i}. {nombre} - {score}"
        mostrar_texto(pantalla, texto, (pos_inicial[0], y), font, color)
        y += 30

def crear_lista_powers(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int):
    lista_respuestas = []

    for i in range(4):
        respuesta = crear_elemento_juego(textura,ancho,alto,pos_x,pos_y)
        lista_respuestas.append(respuesta)
        pos_y += 80    
        
    return lista_respuestas


def eliminar_dos_opciones_incorrectas(pregunta_actual: dict, lista_respuestas: list, correcta: int):
    import random
    incorrectas = [i for i in range(1, 5) if i != correcta]
    eliminadas = random.sample(incorrectas, 2)

    for i in eliminadas:
        limpiar_superficie(lista_respuestas[i - 1], "bloqueada.png", ANCHO_BOTON, ALTO_BOTON)
        mostrar_texto(lista_respuestas[i - 1]["superficie"], "X", (90, 10), FUENTE_RESPUESTA, COLOR_ROJO)

def guardar_estadisticas(lista_preguntas: list):
    import csv
    with open("Preguntas.csv", "w", newline='', encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([
            "pregunta",
            "respuesta_1",
            "respuesta_2",
            "respuesta_3",
            "respuesta_4",
            "respuesta_correcta",
            "veces_preguntada",
            "aciertos",
            "fallos"
        ])
        for p in lista_preguntas:
            escritor.writerow([
                p["pregunta"],
                p["respuesta_1"],
                p["respuesta_2"],
                p["respuesta_3"],
                p["respuesta_4"],
                p["respuesta_correcta"],
                p["veces_preguntada"],
                p["aciertos"],
                p["fallos"]
            ])
    