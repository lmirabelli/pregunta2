import pygame
import csv
import os
import random
import json
from constantes import *

# PANTALLA MENU -----------------------------------------------------------------------------------

def mostrar_texto_menu(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()] 
    space = font.size(' ')[0]
    max_width = surface.get_size()[0] 
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  
                y += word_height  
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  
        y += word_height

# PANTALLA DE JUEGO ----------------------------------------------------------------------------- 

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

def mostrar_texto(texto, x, y, color=BLANCO, fuente=fuente):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

# dividir texto en líneas
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


# PANTALLA CONFIGURACION ------------------------------------------------------------------------

def ajustar_volumen(sonido, volumen):
    sonido.set_volume(volumen)

def dibujar_botones_volumen(pantalla):
    # Dibujar imagen de fondo para botones de volumen música
    pantalla.blit(imagen_boton, (300, 250))
    mostrar_texto(pantalla, "-", (boton_bajar_volumen_musica.centerx, boton_bajar_volumen_musica.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "+", (boton_subir_volumen_musica.centerx, boton_subir_volumen_musica.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "VOLUMEN MUSICA", (boton_volumen_musica.centerx, boton_volumen_musica.centery), fuente, BLANCO)

    # Dibujar imagen de fondo para botones de volumen sonido
    pantalla.blit(imagen_boton, (300, 500))
    mostrar_texto(pantalla, "-", (boton_bajar_volumen_sonido.centerx, boton_bajar_volumen_sonido.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "+", (boton_subir_volumen_sonido.centerx, boton_subir_volumen_sonido.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "VOLUMEN SONIDO", (boton_volumen_sonido.centerx, boton_volumen_sonido.centery), fuente, BLANCO)

def dibujar_boton_volver_menu(pantalla):
    pantalla.blit(imagen_volver_menu, boton_volver_menu_rect.topleft)
    mostrar_texto(pantalla, "VOLVER AL MENU PRINCIPAL", (boton_volver_menu_rect.centerx, boton_volver_menu_rect.centery), fuente, BLANCO)

def mostrar_texto(superficie, texto, posicion, fuente, color):
    texto_superficie = fuente.render(texto, True, color)
    rect_texto = texto_superficie.get_rect(center=posicion)
    superficie.blit(texto_superficie, rect_texto.topleft)

def dibujar_barra_volumen(pantalla, x, y, volumen):
    for i in range(10):
        color = BLANCO if i < volumen * 10 else AZUL
        pygame.draw.rect(pantalla, color, (x + i * 20, y, 18, 30))

# PANTALLA RANKING --------------------------------------------------------------------------------

# Cargar datos del ranking desde un archivo JSON
def cargar_ranking(archivo):
    with open(archivo, "r", encoding="utf-8") as file:
        return json.load(file)

# Ordenar el ranking por puntos de mayor a menor
def obtener_top_10(ranking):
    return sorted(ranking, key=lambda x: x["puntos"], reverse=True)[:10]

# Mostrar ranking en pantalla
def mostrar_ranking(pantalla, top_10):
    pantalla.blit(fondo_ranking, (0, 0))

    # Listar los jugadores y puntos
    y_offset = 50
    for index, jugador in enumerate(top_10):
        # Seleccionar la fuente adecuada según el puesto
        if index == 0:
            fuente_usada = fuente_30
        elif index == 1:
            fuente_usada = fuente_25
        elif index == 2:
            fuente_usada = fuente_22
        else:
            fuente_usada = fuente_20

        texto = f"{index + 1}. {jugador['jugador']}: {jugador['puntos']} puntos"
        texto_render = fuente_usada.render(texto, True, BLANCO)

        # Centramos el texto en la pantalla
        texto_rect = texto_render.get_rect(center=(ANCHO // 2, y_offset))

        # Escalar la imagen de fondo al tamaño del rectángulo
        imagen_fondo_escalada = pygame.transform.scale(pygame.image.load("./img/opcion_default.png"), (texto_rect.width + 40, texto_rect.height + 20))

        # Dibujar la imagen de fondo
        pantalla.blit(imagen_fondo_escalada, (texto_rect.x - 10, texto_rect.y - 10))

        # Dibujar el texto sobre la imagen
        pantalla.blit(texto_render, texto_rect)

        # Espaciado adicional entre filas
        y_offset += 60

    # Mostrar mensaje para regresar al menú
    mensaje = "Presiona ESC para regresar al menú"
    mensaje_render = fuente_30.render(mensaje, True, BLANCO)
    mensaje_rect = mensaje_render.get_rect(center=(ANCHO // 2, ALTO - 50))

    # Escalar y dibujar el fondo para el mensaje
    fondo_mensaje = pygame.transform.scale(pygame.image.load("./img/opcion_incorrecta.png"), (mensaje_rect.width + 80, mensaje_rect.height + 10))
    pantalla.blit(fondo_mensaje, (mensaje_rect.x - 10, mensaje_rect.y - 5))

    # Dibujar el texto del mensaje
    pantalla.blit(mensaje_render, mensaje_rect)