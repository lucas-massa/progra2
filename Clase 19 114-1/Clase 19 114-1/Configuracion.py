import pygame
from Constantes import *
from Funciones import *

pygame.init()

valor_mute = 0
fondo_pantalla = pygame.transform.scale(pygame.image.load("settings.jpg"),PANTALLA)
boton_suma = crear_elemento_juego("mas.webp",60,60,600,200)
boton_resta = crear_elemento_juego("menos.webp",60,60,400,200)
boton_volver = crear_elemento_juego("textura_respuesta.jpg",100,40,10,10)
boton_mute = crear_elemento_juego("mute.png",200,100,600,300)

def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "ajustes"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                #QUE VUELVA AL MENU CUANDO TOCO LA TECLA ESC
                CLICK_SONIDO.play()
                retorno = "menu"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_suma["rectangulo"].collidepoint(evento.pos):
                    if datos_juego["volumen_musica"] <= 95:
                        datos_juego["volumen_musica"] += 5
                        CLICK_SONIDO.play()
                    else:
                        ERROR_SONIDO.play()
                elif boton_resta["rectangulo"].collidepoint(evento.pos):
                    if datos_juego["volumen_musica"] > 0:
                        datos_juego["volumen_musica"] -= 5
                        CLICK_SONIDO.play()
                    else: 
                        ERROR_SONIDO.play()
                elif boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "menu"
                elif boton_mute["rectangulo"].collidepoint(evento.pos):
                    MUTE_SONIDO.play()
                    datos_juego["volumen_musica"] = 0



    pantalla.blit(fondo_pantalla,(0,0))
    pantalla.blit(boton_suma["superficie"],boton_suma["rectangulo"])
    pantalla.blit(boton_resta["superficie"],boton_resta["rectangulo"])
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    pantalla.blit(boton_mute["superficie"],boton_mute["rectangulo"])
    
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(700,200),FUENTE_VOLUMEN,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_RESPUESTA,COLOR_BLANCO)

    return retorno
    
