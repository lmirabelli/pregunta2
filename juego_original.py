import pygame
import time
from datetime import date
from constantes import *
from funciones import *

pygame.init()
reloj = pygame.time.Clock()
ranking_file = "ranking.json"
preguntas = cargar_preguntas("./preguntas.csv")
pregunta_actual = 0
opcion_seleccionada = None
mostrar_respuestas = False
puntaje = 0
vidas = 3
inicio_tiempo = time.time()
boton_pasar_usado = False
contador_bonus = 0
contador = 0
contador_consecutivo = 0
iniciado = False    


mezclar_lista(preguntas)
def manejar_pantalla_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    global pregunta_actual, opcion_seleccionada, mostrar_respuestas, vidas, inicio_tiempo, boton_pasar_usado, puntaje, contador_bonus, contador_consecutivo, bandera_contador, contador, iniciado

    # Inicializamos el cronómetro solo si es la primera vez que accedemos al juego
    if not iniciado:
        inicio_tiempo = time.time()
        iniciado = True 


    contador += 1
    tiempo_actual = 45 - int(time.time() - inicio_tiempo)
    
    if tiempo_actual <= 0:
        if not mostrar_respuestas:
            vidas -= 1
            mostrar_respuestas = True
            sonido_error.play()
        else:
            mostrar_respuestas = False
            opcion_seleccionada = None
            pregunta_actual += 1
            inicio_tiempo = time.time()

        if pregunta_actual >= len(preguntas):
            return "menu"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            return "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN and not mostrar_respuestas:
            x, y = evento.pos
            bandera_contador = contador
            for i, opcion in enumerate(preguntas[pregunta_actual]["opciones"]):
                if 220 <= x <= 820 and 350 + i * 100 <= y <= 400 + i * 100:
                    opcion_seleccionada = opcion
                    mostrar_respuestas = True
                    sonido_tambores.play()
                    pygame.time.wait(1600)
                    if opcion_seleccionada == preguntas[pregunta_actual]["respuesta_correcta"]:
                        puntaje += tiempo_actual
                        sonido_cash.play()
                        contador_consecutivo += 1
                        contador_bonus += 1
                    else:
                        sonido_error.play()
                        puntaje -= 25
                        vidas -= 1
                        contador_consecutivo = 0
                        contador_bonus = 0
                    if contador_consecutivo == 5:
                        vidas += 1
                        sonido_vida.play()
                        contador_consecutivo = 0
                    if contador_bonus == 4:
                        bonus_sound.play()
                        puntaje += tiempo_actual * 10
                        contador_bonus = 0
                if not boton_pasar_usado and 720 <= x <= 920 and 90 <= y <= 140:  # PASAR GDB
                    boton_pasar_usado = True
                    pregunta_actual += 1
                    opcion_seleccionada = None
                    inicio_tiempo = time.time() 
                    mostrar_respuestas = False
                    boton_skip.play()
                if vidas < 1:
                    fecha_actual = date.today()
                    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
                    nuevo_puesto = {"jugador": "", "puntos": puntaje, "fecha": fecha_formateada}

                    with open(ranking_file, "r") as archivo:
                        ranking = json.load(archivo)

                    ranking.append(nuevo_puesto)

                    with open(ranking_file, "w") as archivo:
                        json.dump(ranking, archivo, indent=4)

                    pregunta_actual = 0
                    opcion_seleccionada = None
                    mostrar_respuestas = False
                    puntaje = 0
                    vidas = 3
                    inicio_tiempo = time.time()
                    boton_pasar_usado = False
                    contador_bonus = 0
                    contador = 0
                    contador_consecutivo = 0
                    mezclar_lista(preguntas)
                    iniciado = False

                    return "terminado"
                    
    if contador_bonus == 3:
        pantalla.blit(fondo_bonus, (0, 0))
    else:
        pantalla.blit(fondo, (0, 0))
    # boton_rect = imagen_opcion_default.get_rect(topleft=(650, 500))
    texto_con_borde(pantalla,f"DINERO: ${puntaje}",fuente_juego,NEGRO,BLANCO,(10,10),ancho_borde=2)
    texto_con_borde(pantalla,f"VIDAS: {vidas}",fuente_juego,NEGRO,BLANCO,(10,50),ancho_borde=2)
    texto_con_borde(pantalla,f"{tiempo_actual}s",fuente_juego,NEGRO,BLANCO,(500,40),ancho_borde=3)

    if pregunta_actual < len(preguntas):
        pregunta = preguntas[pregunta_actual]["pregunta"]
        opciones = preguntas[pregunta_actual]["opciones"]
        respuesta_correcta = preguntas[pregunta_actual]["respuesta_correcta"]

        mostrar_pregunta_con_imagen(pregunta, 200, 150)

        for i, opcion in enumerate(opciones):
            if mostrar_respuestas:
                if opcion == respuesta_correcta:
                    pantalla.blit(imagen_opcion_correcta, (220, 350 + i * 100))
                elif opcion == opcion_seleccionada:
                    pantalla.blit(imagen_opcion_incorrecta, (220, 350 + i * 100))
                else:
                    pantalla.blit(imagen_opcion_default, (220, 350 + i * 100))
            else:
                pantalla.blit(imagen_opcion_default, (220, 350 + i * 100))
            texto_con_borde(pantalla,opcion,fuente_pequeña,NEGRO,BLANCO,(255, 365 + i * 100),ancho_borde=2)

        if boton_pasar_usado:
            pantalla.blit(imagen_boton_skip_incorrecta, (690, 92))
        else:
            pantalla.blit(imagen_boton_skip_default, (690, 92))
        texto_con_borde(pantalla,"PASAR TURNO",fuente_juego,NEGRO,BLANCO,( 720, 100), ancho_borde=2)

    if mostrar_respuestas and contador == (bandera_contador + 10):
        pygame.time.delay(1000)
        mostrar_respuestas = False
        opcion_seleccionada = None
        pregunta_actual += 1
        inicio_tiempo = time.time()
        if pregunta_actual >= len(preguntas):
            return "menu"
    

    pygame.display.flip()
    return "juego"