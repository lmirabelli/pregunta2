import pygame
import csv
import os
import time
import random
from constantes import *

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

# Función para mostrar texto
def mostrar_texto(texto, x, y, color=BLANCO, fuente=fuente):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))


def mostrar_texto_menu(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

# Función para dividir texto en líneas
def ajustar_texto(texto, fuente, ancho_max):
    palabras = texto.split(" ")
    lineas = []
    linea_actual = ""
    
    for palabra in palabras:
        # Verificar si la línea actual con la nueva palabra cabe en el ancho
        if fuente.size(linea_actual + palabra + " ")[0] <= ancho_max:
            linea_actual += palabra + " "
        else:
            # Si no cabe, agregar la línea actual a las líneas y empezar una nueva
            lineas.append(linea_actual.strip())
            linea_actual = palabra + " "
    
    # Agregar la última línea si queda algo
    if linea_actual:
        lineas.append(linea_actual.strip())
    
    return lineas

# Mostrar pregunta con fondo de imagen y texto ajustado
def mostrar_pregunta_con_imagen(texto, x, y, color_texto=BLANCO, ancho_max=580):
    lineas = ajustar_texto(texto, fuente, ancho_max)
    espacio_entre_lineas = 30  # Espaciado entre líneas
    
    # Calcular altura total del texto
    altura_total = len(lineas) * fuente.get_height() + (len(lineas) - 1) * espacio_entre_lineas

    # Calcular posición inicial para centrar el texto en el rectángulo
    y_inicial = y + (fondo_pregunta.get_height() - altura_total) // 2

    # Dibujar el fondo
    pantalla.blit(fondo_pregunta, (x, y))

    # Dibujar cada línea de texto
    for i, linea in enumerate(lineas):
        mostrar_texto(linea, x + 20, y_inicial + i * (fuente.get_height() + espacio_entre_lineas), color=color_texto)

# Mezclar preguntas
def mezclar_lista(lista_preguntas):
    random.shuffle(lista_preguntas)