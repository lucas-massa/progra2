import pygame
from Constantes import *
from Funciones import *

pygame.init()
bandera_juego = False
fuente = pygame.font.SysFont("Arial Narrow",40)
cuadro = crear_elemento_juego("textura_respuesta.jpg",250,50,200,270)
fondo_pantalla = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)
boton_volver = crear_elemento_juego("textura_respuesta.jpg",100,40,10,10)


def mostrar_fin_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict, lista_preguntas: list) -> str:
    retorno = "terminado"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"

        elif evento.type == pygame.KEYDOWN:
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            letra_presionada = pygame.key.name(evento.key)

            if letra_presionada == "backspace" and len(datos_juego["nombre"]) > 0:
                datos_juego["nombre"] = datos_juego["nombre"][:-1]
                limpiar_superficie(cuadro, "textura_respuesta.jpg", 250, 50)

            if letra_presionada == "space":
                datos_juego["nombre"] += " "

            if len(letra_presionada) == 1:
                if bloc_mayus != 0:
                    datos_juego["nombre"] += letra_presionada.upper()
                else:
                    datos_juego["nombre"] += letra_presionada

            if evento.key == pygame.K_ESCAPE:
                guardar_ranking(datos_juego["nombre"], datos_juego["puntuacion"])
                guardar_estadisticas(lista_preguntas)  # Guardamos estadísticas actualizadas
                retorno = "salir"

    pantalla.blit(fondo_pantalla, (0, 0))
    pantalla.blit(cuadro["superficie"], cuadro["rectangulo"])

    mostrar_texto(cuadro["superficie"], datos_juego["nombre"], (10, 0), fuente, COLOR_BLANCO)
    mostrar_texto(pantalla, f"Usted obtuvo: {datos_juego['puntuacion']} puntos", (250, 100), fuente, COLOR_NEGRO)

    if datos_juego.get("comodines_usados"):
        usados = ", ".join(datos_juego["comodines_usados"])
        mostrar_texto(pantalla, f"Comodines usados: {usados}", (250, 150), fuente, COLOR_NEGRO)

    # Mostrar estadisticas de la sesión actual
    aciertos = datos_juego.get("aciertos_en_sesion", 0)
    respondidas = datos_juego.get("preguntas_respondidas_en_sesion", 0)

    if respondidas > 0:
        porcentaje = int((aciertos / respondidas) * 100)
        mostrar_texto(pantalla, f"Estadísticas de esta partida: {porcentaje}% ({aciertos}/{respondidas})", (250, 200), fuente, COLOR_NEGRO)
    else:
        mostrar_texto(pantalla, "No se respondieron preguntas esta sesión.", (250, 200), fuente, COLOR_NEGRO)

    return retorno