import pygame
from Constantes import *
from Funciones import *

pygame.init()

boton_volver = crear_elemento_juego("textura_respuesta.jpg",100,40,10,10)
fondo_pantalla = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)


def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],lista_rankings:list) -> str:
    retorno = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "menu"
    
    pantalla.blit(fondo_pantalla,(0,0))
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_RESPUESTA,COLOR_BLANCO)

    top10 = obtener_top_10("ranking.json")  # O el nombre de tu archivo

    y = 100
    mostrar_texto(pantalla, "TOP 10", (150, 50), FUENTE_VOLUMEN, COLOR_NEGRO)
    y += 40

    for i, fila in enumerate(top10):
        if i == 0:
            texto = f"{fila[0]:10} | {fila[1]:5} | {fila[2]}"
        else:
            texto = f"{fila[0]:10} | {fila[1]:5} | {fila[2]}"
        mostrar_texto(pantalla, texto, (100, y), FUENTE_RESPUESTA, COLOR_NEGRO)
        y += 30

    return retorno
    