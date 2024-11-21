import pygame
import json
import os
import time
import random

pygame.init()
reloj = pygame.time.Clock()
# Configuración de la pantalla
ANCHO, ALTO = 1080, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Preguntados - el equipo del canal cultural")
icono = pygame.image.load("./img/icono.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("./img/fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Sonidos
sonido_cash = pygame.mixer.Sound("./sound/cash_sound.mp3")
sonido_cash.set_volume(1)
sonido_tambores = pygame.mixer.Sound("./sound/tambores.mp3")
sonido_tambores.set_volume(0.2)
sonido_error = pygame.mixer.Sound("./sound/sonido_error.mp3")
sonido_error.set_volume(0.2)

#MUSICA
pygame.mixer.init()
pygame.mixer.music.load(".\sound\musica.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

# Cargar imagen de fondo para la pregunta
fondo_pregunta = pygame.image.load("./img/fondo_pregunta.png")
fondo_pregunta = pygame.transform.scale(fondo_pregunta, (650, 100))  # Ajustar tamaño

# Cargar texturas para las opciones
imagen_opcion_default = pygame.image.load("./img/opcion_default.png")
imagen_opcion_correcta = pygame.image.load("./img/opcion_correcta.png")
imagen_opcion_incorrecta = pygame.image.load("./img/opcion_incorrecta.png")
imagen_opcion_default = pygame.transform.scale(imagen_opcion_default, (600, 50))
imagen_opcion_correcta = pygame.transform.scale(imagen_opcion_correcta, (600, 50))
imagen_opcion_incorrecta = pygame.transform.scale(imagen_opcion_incorrecta, (600, 50))

# Colores
NEGRO = (18, 18, 18)
BLANCO = (245, 245, 245)

# Fuentes
fuente = pygame.font.Font(None, 30)
fuente_grande = pygame.font.Font(None, 60)

# Cargar preguntas desde JSON
def cargar_preguntas(ruta):
    print(os.path.abspath(ruta))
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

preguntas = cargar_preguntas("./preguntas.json")
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
def mostrar_pregunta_con_imagen(texto, x, y, color_texto=NEGRO):
    pantalla.blit(fondo_pregunta, (x, y))
    mostrar_texto(texto, x + 20, y + 33, color=color_texto)

# Mezclar preguntas
def mezclar_lista(lista_preguntas):
    random.shuffle(lista_preguntas)

# Bucle principal
ejecutando = True
mezclar_lista(preguntas)
contador = 0
# bandera_click = False
while ejecutando:
    contador += 1
    pygame.event.clear(pygame.MOUSEBUTTONDOWN) 
    # if bandera_click == True:
    #     bandera_click = False

    reloj.tick(30)
    tiempo_actual = 45 - int(time.time() - inicio_tiempo)
    if tiempo_actual <= 0:
        mostrar_respuestas = True
        tiempo_actual = 0

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and not mostrar_respuestas:
            x, y = evento.pos
            bandera_contador = contador
            for i, opcion in enumerate(preguntas[pregunta_actual]["opciones"]):
                if 220 <= x <= 820 and 350 + i * 100 <= y <= 400 + i * 100:
                    # bandera_click = True
                    # print(bandera_click)
                    
                    opcion_seleccionada = opcion
                    mostrar_respuestas = True
                    sonido_tambores.play()
                    pygame.time.wait(1600)
                    if opcion_seleccionada == preguntas[pregunta_actual]["respuesta_correcta"]:
                        puntaje += tiempo_actual
                        sonido_cash.play()
                    else:
                        sonido_error.play()
                        puntaje -= 25
                        vidas -= 1

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
    print(contador)



    if mostrar_respuestas and contador == (bandera_contador + 10):
        pygame.time.delay(1000)
        # print(bandera_click)
        mostrar_respuestas = False
        opcion_seleccionada = None
        pregunta_actual += 1
        inicio_tiempo = time.time()
        if pregunta_actual >= len(preguntas):
            ejecutando = False
    pygame.display.flip()

pygame.quit()