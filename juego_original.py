import pygame
import time
import random
from constantes import *
from funciones import *

pygame.init()
reloj = pygame.time.Clock()

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

# Función para mostrar texto
def mostrar_texto(texto, x, y, color=BLANCO, fuente=fuente):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

# Mostrar pregunta con fondo de imagen
def mostrar_pregunta_con_imagen(texto, x, y, color_texto=BLANCO):
    pantalla.blit(fondo_pregunta, (x, y))
    mostrar_texto(texto, x + 20, y + 42, color=color_texto)

# Mezclar preguntas
def mezclar_lista(lista_preguntas):
    random.shuffle(lista_preguntas)

mezclar_lista(preguntas)

def manejar_pantalla_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    global pregunta_actual, opcion_seleccionada, mostrar_respuestas, puntaje, vidas, inicio_tiempo, boton_pasar_usado, contador_bonus, contador_consecutivo, bandera_contador, contador

    contador += 1
    tiempo_actual = 45 - int(time.time() - inicio_tiempo)
    if tiempo_actual <= 0:
        if not mostrar_respuestas:
            vidas -= 1
            mostrar_respuestas = True
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
                    else:
                        sonido_error.play()
                        puntaje -= 25
                        vidas -= 1
                        contador_consecutivo = 0
                    if contador_consecutivo == 5:
                        vidas += 1
                        sonido_vida.play()
                        contador_consecutivo = 0
                    if contador_consecutivo >= 7:
                        bonus_sound.play()
                        puntaje += 25 * 2
                        contador_bonus += 1
                    if contador_bonus == 3:
                        contador_bonus = 0
                if not boton_pasar_usado and 720 <= x <= 920 and 90 <= y <= 140:  # PASAR GDB
                    boton_pasar_usado = True
                    pregunta_actual += 1
                    opcion_seleccionada = None
                    inicio_tiempo = time.time()
                    mostrar_respuestas = False
                    boton_skip.play()

    pantalla.blit(fondo, (0, 0))
    boton_rect = imagen_opcion_default.get_rect(topleft=(650, 500))
    mostrar_texto(f"Puntaje: {puntaje}", 10, 10)
    mostrar_texto(f"Vidas: {vidas} ({contador_consecutivo})", 10, 50)
    mostrar_texto(f"{tiempo_actual}s", 530, 40, color=BLANCO, fuente=fuente_grande)

    if pregunta_actual < len(preguntas):
        pregunta = preguntas[pregunta_actual]["pregunta"]
        opciones = preguntas[pregunta_actual]["opciones"]
        respuesta_correcta = preguntas[pregunta_actual]["respuesta_correcta"]

        mostrar_pregunta_con_imagen(pregunta, 222, 150)

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
            mostrar_texto(opcion, 235, 365 + i * 100, BLANCO)

        if boton_pasar_usado:
            pantalla.blit(imagen_boton_skip_incorrecta, (720, 90))
        else:
            pantalla.blit(imagen_boton_skip_default, (720, 90))
        mostrar_texto("Pasar turno", 760, 103, BLANCO)

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

