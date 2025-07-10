import pygame 
from Constantes import *
from Menu import *
from Juego import *
from Configuracion import *
from Rankings import *
from Terminado import *
import json
import os
from Funciones import *

lista_preguntas = []
leer_csv_alumnos("Preguntas.csv",lista_preguntas)

mezclar_lista(lista_preguntas)
print(lista_preguntas[0])

pygame.init()
pygame.display.set_caption("PREGUNTADOS 114")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)

pantalla = pygame.display.set_mode(PANTALLA)
corriendo = True
datos_juego = {"puntuacion":0,"vidas":3,"nombre":"","tiempo_restante":TIEMPO_JUEGO,"volumen_musica":10,"indice":0,"conteo_correctas":0,"preguntas_respondidas_en_sesion": 0,
"aciertos_en_sesion": 0,"comodines_usados":[]}

#lista_rankings = cargo el json
lista_rankings  = []
reloj = pygame.time.Clock()
ventana_actual = "menu"

bandera_juego = False

while corriendo:
    reloj.tick(FPS)
    #El manejo de eventos no lo hacemos aca, pero tenemos que generar la cola de eventos
    cola_eventos = pygame.event.get()
    
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "salir":
        guardar_estadisticas(lista_preguntas)  #Guardamos al salir
        corriendo = bandera_juego
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos,lista_rankings)
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "juego":
        if bandera_juego == False:
            pygame.mixer.init()
            pygame.mixer.music.load("fondo_music.mp3")
            porcentaje_musica = datos_juego["volumen_musica"] / 100
            pygame.mixer.music.set_volume(porcentaje_musica)
            pygame.mixer.music.play(-1)
            bandera_juego = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego,lista_preguntas)
    elif ventana_actual == "terminado":
        if bandera_juego == True:
            bandera_juego = False
            pygame.mixer.music.stop()
        ventana_actual = mostrar_fin_juego(pantalla, cola_eventos, datos_juego, lista_preguntas)
    
    #print(f"USTED ESTA PARADO EN LA VENTANA: {ventana_actual}")
    
    pygame.display.flip()

pygame.quit()
