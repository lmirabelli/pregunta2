import pygame
import csv
import os
import time
import random
from constantes import *

pygame.init()
reloj = pygame.time.Clock()

# Cargar preguntas desde CSV
def cargar_preguntas(ruta):
    print(os.path.abspath(ruta))
    preguntas = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            pregunta = {
                "pregunta": fila["pregunta"],
                "opciones": [fila["opcion1"], fila["opcion2"], fila["opcion3"], fila["opcion4"]],
                "respuesta_correcta": fila["respuesta_correcta"],
            }
            preguntas.append(pregunta)
    return preguntas

preguntas = cargar_preguntas("./preguntas.csv")
pregunta_actual = 0
opcion_seleccionada = None
mostrar_respuestas = False
puntaje = 0
vidas = 3
inicio_tiempo = time.time()

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

# Bucle principal
ejecutando = True
mezclar_lista(preguntas)
contador = 0
bandera_click = False
contador_consecutivo = 0
while ejecutando:
    contador += 1
    pygame.event.clear(pygame.MOUSEBUTTONDOWN) 
    reloj.tick(30)
    tiempo_actual = 45 - int(time.time() - inicio_tiempo)
    if tiempo_actual <= 0:
        if not mostrar_respuestas:
        # Si el tiempo llegó a 0 y aún no se han mostrado las respuestas:
            vidas -= 1  # Se pierde una vida
            mostrar_respuestas = True
        else:
        # Pasar a la siguiente pregunta
            mostrar_respuestas = False
            opcion_seleccionada = None
            pregunta_actual += 1
            inicio_tiempo = time.time()  # Reinicia el temporizador

        # Si ya no hay más preguntas, regresar al menú
        if pregunta_actual >= len(preguntas):
            estado_actual = "menu"
            inicio_tiempo = None  # Detener el tiempo

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
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

    pantalla.blit(fondo, (0, 0))
    mostrar_texto(f"Puntaje: {puntaje}", 10, 10)
    mostrar_texto(f"Vidas: {vidas}", 10, 50)

    
    mostrar_texto(f"{tiempo_actual}s", 530, 40, color=BLANCO, fuente=fuente_grande)
    if pregunta_actual < len(preguntas):
        pregunta = preguntas[pregunta_actual]["pregunta"]
        opciones = preguntas[pregunta_actual]["opciones"]
        respuesta_correcta = preguntas[pregunta_actual]["respuesta_correcta"]

        # Mostrar pregunta con imagen de fondo
        mostrar_pregunta_con_imagen(pregunta, 222, 150)

        # Mostrar opciones con texturas
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



    if mostrar_respuestas and contador == (bandera_contador + 10):
        pygame.time.delay(1000)
        mostrar_respuestas = False
        opcion_seleccionada = None
        pregunta_actual += 1
        inicio_tiempo = time.time()
        if pregunta_actual >= len(preguntas):
            ejecutando = False
    pygame.display.flip()

pygame.quit()