import pygame 
from Constantes import *
from leer_csv import *
from Funciones import *


pygame.init()
fondo_pantalla = pygame.transform.scale(pygame.image.load("momo_fondo1.jpeg"),PANTALLA)
cuadro_pregunta = crear_elemento_juego("textura_pregunta.jpg",ANCHO_PREGUNTA,ALTO_PREGUNTA,80,80)
lista_respuestas = crear_lista_powers("textura_respuesta.jpg",ANCHO_BOTON,ALTO_BOTON,125,245)
evento_tiempo = pygame.USEREVENT 
pygame.time.set_timer(evento_tiempo,1000)

imagenes_comodines = ["bomba.png", "x2.png", "doble_chance.png", "pasar.png"]
tipos_comodines = ["BOMBA", "X2", "DOBLE CHANCE", "PASAR"]
lista_comodines = []
comodines_usados = {}

for i in range(len(imagenes_comodines)):
    boton = crear_elemento_juego(imagenes_comodines[i], 60, 60, 980, 80 + i * 70)
    lista_comodines.append(boton)
    comodines_usados[tipos_comodines[i]] = False

respuestas_bloqueadas = set()  

def mostrar_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict, lista_preguntas: list) -> str:
    retorno = "juego"
    pregunta_actual = lista_preguntas[datos_juego["indice"]]
    pregunta_actual["veces_preguntada"] += 1  # Se cuenta como mostrada

    if datos_juego["vidas"] == 0 or datos_juego["tiempo_restante"] == 0:
        print("GAME OVER")
        retorno = "terminado"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"

        elif evento.type == evento_tiempo:
            datos_juego["tiempo_restante"] -= 1

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                # --- CLICK EN RESPUESTA ---
                for i in range(len(lista_respuestas)):
                    if lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                        if i in respuestas_bloqueadas:
                            continue

                        respuesta = i + 1
                        datos_juego["preguntas_respondidas_en_sesion"] += 1  

                        if pregunta_actual["respuesta_correcta"] == respuesta:
                            CLICK_SONIDO.play()

                            puntos = PUNTUACION_ACIERTO
                            if datos_juego.get("doble_puntaje"):
                                puntos *= 2
                                datos_juego["doble_puntaje"] = False

                            datos_juego["puntuacion"] += puntos
                            datos_juego["conteo_correctas"] += 1
                            datos_juego["aciertos_en_sesion"] += 1        #  Contar acierto en sesión
                            pregunta_actual["aciertos"] += 1              #  Historial total

                            if datos_juego["conteo_correctas"] == 5:
                                datos_juego["vidas"] += 2
                                datos_juego["tiempo_restante"] += 5
                                datos_juego["conteo_correctas"] = 0

                            datos_juego["segunda_chance"] = False
                            respuestas_bloqueadas.clear()

                            datos_juego["indice"] += 1
                            if datos_juego["indice"] >= len(lista_preguntas):
                                datos_juego["indice"] = 0
                                mezclar_lista(lista_preguntas)

                            pregunta_actual = pasar_pregunta(lista_preguntas, datos_juego["indice"], cuadro_pregunta, lista_respuestas)

                        else:
                            if datos_juego.get("segunda_chance", False):
                                datos_juego["segunda_chance"] = False
                                limpiar_superficie(lista_respuestas[i], "bloqueada.png", ANCHO_BOTON, ALTO_BOTON)
                                mostrar_texto(lista_respuestas[i]["superficie"], "X", (90, 10), FUENTE_RESPUESTA, COLOR_ROJO)
                                respuestas_bloqueadas.add(i)
                            else:
                                pregunta_actual["fallos"] += 1  # Historial total
                                ERROR_SONIDO.play()
                                datos_juego["puntuacion"] -= PUNTUACION_ERROR
                                datos_juego["vidas"] -= 1
                                datos_juego["conteo_correctas"] = 0
                                respuestas_bloqueadas.clear()

                                datos_juego["indice"] += 1
                                if datos_juego["indice"] >= len(lista_preguntas):
                                    datos_juego["indice"] = 0
                                    mezclar_lista(lista_preguntas)

                                pregunta_actual = pasar_pregunta(lista_preguntas, datos_juego["indice"], cuadro_pregunta, lista_respuestas)

                # --- CLICK EN COMODÍN ---
                for i, boton in enumerate(lista_comodines):
                    if boton["rectangulo"].collidepoint(evento.pos) and not comodines_usados[tipos_comodines[i]]:
                        tipo = tipos_comodines[i]
                        comodines_usados[tipo] = True
                        datos_juego["comodines_usados"].append(tipo)

                        if tipo == "BOMBA":
                            eliminar_dos_opciones_incorrectas(pregunta_actual, lista_respuestas, pregunta_actual["respuesta_correcta"])
                        elif tipo == "X2":
                            datos_juego["doble_puntaje"] = True
                        elif tipo == "DOBLE CHANCE":
                            datos_juego["segunda_chance"] = True
                        elif tipo == "PASAR":
                            datos_juego["indice"] += 1
                            if datos_juego["indice"] >= len(lista_preguntas):
                                datos_juego["indice"] = 0
                                mezclar_lista(lista_preguntas)
                            pregunta_actual = pasar_pregunta(lista_preguntas, datos_juego["indice"], cuadro_pregunta, lista_respuestas)
                            respuestas_bloqueadas.clear()

    # --- DIBUJO EN PANTALLA ---
    pantalla.blit(fondo_pantalla, (0, 0))
    pantalla.blit(cuadro_pregunta["superficie"], cuadro_pregunta["rectangulo"])

    for i in range(len(lista_respuestas)):
        pantalla.blit(lista_respuestas[i]["superficie"], lista_respuestas[i]["rectangulo"])

    for i, boton in enumerate(lista_comodines):
        if not comodines_usados[tipos_comodines[i]]:
            pantalla.blit(boton["superficie"], boton["rectangulo"])

    mostrar_texto(cuadro_pregunta["superficie"], pregunta_actual["pregunta"], (15, 15), FUENTE_PREGUNTA, COLOR_NEGRO)
    for i in range(4):
        mostrar_texto(lista_respuestas[i]["superficie"], pregunta_actual[f"respuesta_{i+1}"], (15, 15), FUENTE_RESPUESTA, COLOR_BLANCO)

    mostrar_texto(pantalla, f"VIDAS: {datos_juego['vidas']}", (10, 10), FUENTE_TEXTO, COLOR_NEGRO)
    mostrar_texto(pantalla, f"PUNTUACION: {datos_juego['puntuacion']}", (10, 40), FUENTE_TEXTO, COLOR_NEGRO)
    mostrar_texto(pantalla, f"TIEMPO: {datos_juego['tiempo_restante']} seg", (900, 10), FUENTE_TEXTO, COLOR_NEGRO)

    return retorno
