import pygame
import json
import os
import time

pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 1080, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Preguntados - el equipo del canal cultural")
icono = pygame.image.load("img/favicon.jpg")  # Ruta al archivo del ícono
pygame.display.set_icon(icono)
fondo = pygame.image.load("img/planisferio.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Colores
NEGRO = (18, 18, 18)
AZUL = (70, 130, 180)
VERDE = (50, 121, 30)
ROJO = (190, 69, 0)
BLANCO = (245, 245, 245)

# Fuentes
fuente = pygame.font.Font(None, 30)
fuente_grande = pygame.font.Font(None, 100)  

# Cargar preguntas desde JSON
def cargar_preguntas(ruta):
    print(os.path.abspath(ruta))
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

preguntas = cargar_preguntas("preguntas.json")
pregunta_actual = 0
opcion_seleccionada = None
mostrar_respuestas = False
puntaje = 0
tiempo_restante = 45  
vidas = 3  
inicio_tiempo = time.time()  

# Función para mostrar texto en pantalla
def mostrar_texto(texto, x, y, color=NEGRO, fuente=fuente):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

def mostrar_pregunta_con_fondo(texto, x, y, color_texto=NEGRO, color_fondo=BLANCO, ancho=960, alto=100):
    pygame.draw.rect(pantalla, color_fondo, (x, y, ancho, alto))
    mostrar_texto(texto, x + 10, y + 10, color_texto)

# Bucle principal de Pygame
ejecutando = True
while ejecutando:
    # Calcular el tiempo restante
    tiempo_actual = 45 - int(time.time() - inicio_tiempo)
    if tiempo_actual <= 0:
        mostrar_respuestas = True
        tiempo_actual = 0
        if not opcion_seleccionada:
            puntaje -= 50

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and not mostrar_respuestas:
            # Obtener la posición del clic
            x, y = evento.pos
            for i, opcion in enumerate(preguntas[pregunta_actual]["opciones"]):
                # Verificar si se hace clic en una opción
                if 100 <= x <= 700 and 350 + i * 100 <= y <= 400 + i * 100:
                    opcion_seleccionada = opcion
                    mostrar_respuestas = True
                    if opcion_seleccionada == preguntas[pregunta_actual]["respuesta_correcta"]:
                        puntaje += tiempo_actual 
                    else:
                        puntaje -= 25
                        vidas -= 1  

    pantalla.blit(fondo, (0, 0))

    # Mostrar puntaje y vidas
    mostrar_texto(f"Puntaje: {puntaje}", 10, 10)
    mostrar_texto(f"Vidas: {vidas}", 10, 50)

    # Mostrar temporizador
    mostrar_texto(f"Tiempo: {tiempo_actual}s", 10, 90)

    # Comprobar si el jugador se quedó sin vidas
    if vidas <= 0:
        pantalla.fill(NEGRO)
        mostrar_texto("¡Juego Terminado!", ANCHO // 2 - 200, ALTO // 3, BLANCO, fuente_grande)
        mostrar_texto(f"Tu puntaje final es: {puntaje}", ANCHO // 2 - 200, ALTO // 2, BLANCO, fuente_grande)
        pygame.display.flip()
        pygame.time.wait(3000) 
        ejecutando = False

    # Obtener la pregunta y las opciones actuales
    if pregunta_actual < len(preguntas):
        pregunta = preguntas[pregunta_actual]["pregunta"]
        opciones = preguntas[pregunta_actual]["opciones"]
        respuesta_correcta = preguntas[pregunta_actual]["respuesta_correcta"]

        # Mostrar Pregunta
        mostrar_pregunta_con_fondo(pregunta, 50, 150)

        # Mostrar las opciones
        for i, opcion in enumerate(opciones):
            color_fondo = AZUL
            if mostrar_respuestas:
                if opcion == respuesta_correcta:
                    color_fondo = VERDE 
                elif opcion == opcion_seleccionada:
                    color_fondo = ROJO 

            pygame.draw.rect(pantalla, color_fondo, (100, 350 + i * 100, 600, 50))
            mostrar_texto(opcion, 110, 360 + i * 100, BLANCO)

    pygame.display.flip()

    if mostrar_respuestas:
        pygame.time.wait(1000)  # Esperar 1 segundo
        mostrar_respuestas = False
        opcion_seleccionada = None
        pregunta_actual += 1
        inicio_tiempo = time.time() 

        if pregunta_actual >= len(preguntas):
            ejecutando = False

pygame.quit()
