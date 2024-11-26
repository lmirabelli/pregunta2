import pygame
import json
from constantes import *
from funciones import *
from juego_original import puntaje

pygame.init()

ranking_file = "ranking.json"

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Fuentes
pygame.font.init()
fuente = pygame.font.Font(None, 36)

# Elementos estáticos
input_box = pygame.Rect(440, 300, 200, 50)
boton_guardar = pygame.Rect(440, 400, 200, 50)
texto_nombre = ''
mensaje = ''

def agregar_puesto_ranking(pantalla, cola_eventos):
    global texto_nombre, mensaje
    
    # Dibujar fondo
    pantalla.fill(BLANCO)
    pantalla.blit(fondo_ranking, (0, 0))
    
    # Mostrar puntaje actual
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, NEGRO)
    pantalla.blit(texto_puntaje, (440, 200))
    
    # Mostrar input box
    pygame.draw.rect(pantalla, NEGRO, input_box, 2)
    texto_input = fuente.render(texto_nombre, True, NEGRO)
    pantalla.blit(texto_input, (input_box.x + 10, input_box.y + 10))
    
    # Mostrar botón guardar
    pygame.draw.rect(pantalla, NEGRO, boton_guardar)
    texto_boton = fuente.render("Guardar puntaje", True, BLANCO)
    pantalla.blit(texto_boton, (boton_guardar.x + 20, boton_guardar.y + 10))
    
    # Mostrar mensaje
    if mensaje:
        texto_mensaje = fuente.render(mensaje, True, NEGRO)
        pantalla.blit(texto_mensaje, (440, 500))

    # Manejo de eventos
    for evento in cola_eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                mensaje = guardar_puntaje(texto_nombre, puntaje)
            elif evento.key == pygame.K_BACKSPACE:
                texto_nombre = texto_nombre[:-1]
            else:
                texto_nombre += evento.unicode

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_guardar.collidepoint(evento.pos):
                mensaje = guardar_puntaje(texto_nombre, puntaje)
    
    pygame.display.flip()
    if mensaje == "¡Puntaje guardado!":
        return "ranking"
    else:
        return "terminado"  # Retorna al menú de ranking si es necesario.

def guardar_puntaje(nombre, puntaje):
    if not nombre.strip():
        return "Ingresa un nombre válido."
    
    nuevo_puesto = {"jugador": nombre.strip(), "puntos": puntaje}
    
    try:
        with open(ranking_file, "r") as archivo:
            ranking = json.load(archivo)
    except FileNotFoundError:
        ranking = []

    ranking.append(nuevo_puesto)
    
    with open(ranking_file, "w") as archivo:
        json.dump(ranking, archivo, indent=4)
    
    return "¡Puntaje guardado!"
