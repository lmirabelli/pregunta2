import pygame
import csv
import os
import random
import json
from constantes import *

# PANTALLA MENU -----------------------------------------------------------------------------------

def mostrar_texto_menu(surface, text, pos, font, color=pygame.Color('black')):
    palabras = [word.split(' ') for word in text.splitlines()] 
    space = font.size(' ')[0]
    max_width = surface.get_size()[0] 
    x, y = pos
    for line in palabras:
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
def texto_con_borde(
    pantalla: pygame.Surface,
    texto: str,
    fuente: pygame.font.Font,
    color_texto: tuple,
    color_borde: tuple,
    posicion: tuple,
    ancho_borde: int = 2
):
    # Renderizar el texto
    superficie_texto = fuente.render(texto, True, color_texto)
    superficie_borde = fuente.render(texto, True, color_borde)

    # Dibujar el texto del borde desplazado en las 8 direcciones cardinales
    x, y = posicion
    for dx in [-ancho_borde, 0, ancho_borde]:
        for dy in [-ancho_borde, 0, ancho_borde]:
            if dx != 0 or dy != 0:  # Evitar el centro
                pantalla.blit(superficie_borde, (x + dx, y + dy))

    # Dibujar el texto principal
    pantalla.blit(superficie_texto, (x, y))

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

def ajustar_texto(texto, fuente, ancho_max, alto_max):
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
    
    # Verificar que las líneas no se desborden verticalmente
    total_altura = len(lineas) * fuente.get_height() + (len(lineas) - 1) * 10  # Ajuste de espacio entre líneas
    if total_altura > alto_max:
        lineas = lineas[:int(alto_max / (fuente.get_height() + 10))]  # Recortar las líneas si el texto excede el área
    return lineas

def mostrar_pregunta_con_imagen(texto, x, y, color_texto=BLANCO, ancho_max=580, alto_max=350):
    # Ajustar texto según el tamaño máximo disponible
    lineas = ajustar_texto(texto, fuente_pequeña, ancho_max, alto_max)
    espacio_entre_lineas = 30  # Espaciado entre líneas
    
    # Calcular altura total del texto ajustado
    altura_total = len(lineas) * fuente_pequeña.get_height() + (len(lineas) - 1) * espacio_entre_lineas

    # Calcular posición inicial para centrar el texto en el rectángulo
    y_inicial = y + (alto_max - altura_total) // 2  # Se asegura de que no se desborde

    # Dibujar el fondo de la pregunta
    pantalla.blit(fondo_pregunta, (x, y))

    # Dibujar cada línea de texto ajustado
    for i, linea in enumerate(lineas):
        mostrar_texto(linea, x + 20, y_inicial + i * (fuente_pequeña.get_height() + espacio_entre_lineas), color=color_texto)

# Mezclar preguntas
def mezclar_lista(lista_preguntas):
    random.shuffle(lista_preguntas)


# PANTALLA CONFIGURACION ------------------------------------------------------------------------

def ajustar_volumen(sonido, volumen):
    sonido.set_volume(volumen)

def dibujar_botones_volumen(pantalla):
    # Dibujar imagen de fondo para botones de volumen música
    pantalla.blit(imagen_boton, (340, 250))
    mostrar_texto(pantalla, "-", (boton_bajar_volumen_musica.centerx, boton_bajar_volumen_musica.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "+", (boton_subir_volumen_musica.centerx, boton_subir_volumen_musica.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "VOLUMEN MUSICA", (boton_volumen_musica.centerx, boton_volumen_musica.centery), fuente, BLANCO)

    # Dibujar imagen de fondo para botones de volumen sonido
    pantalla.blit(imagen_boton, (340, 500))
    mostrar_texto(pantalla, "-", (boton_bajar_volumen_sonido.centerx, boton_bajar_volumen_sonido.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "+", (boton_subir_volumen_sonido.centerx, boton_subir_volumen_sonido.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "VOLUMEN SONIDO", (boton_volumen_sonido.centerx, boton_volumen_sonido.centery), fuente, BLANCO)

def dibujar_boton_volver_menu(pantalla):
    pantalla.blit(imagen_volver_menu, boton_volver_menu_rect.topleft)
    mostrar_texto(pantalla, "VOLVER AL MENU PRINCIPAL", (520,675), fuente_grande_configuraciones, BLANCO)

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
    pantalla.blit(fondo_mensaje, (mensaje_rect.x - 45, mensaje_rect.y - 5))

    # Dibujar el texto del mensaje
    pantalla.blit(mensaje_render, mensaje_rect)

# Función para mostrar texto

def mostrar_texto_vidas(texto, x, y, color=BLANCO, fuente=fuente_juego):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

def mostrar_pregunta_con_imagen(texto, x, y, color_texto=BLANCO):
    pantalla.blit(fondo_pregunta, (x-100, y))
    if len(texto) > 55:
        texto_con_borde(pantalla,texto,fuente_preguntas,NEGRO,BLANCO,(x - 90, y + 37),ancho_borde=2) # CAMBIAR DE POSICION LA PREGUNTA 
    else:
        texto_con_borde(pantalla,texto,fuente_preguntas,NEGRO,BLANCO,(x + 110, y + 37),ancho_borde=2) # CAMBIAR DE POSICION LA PREGUNTA 


# Mezclar preguntas
def mezclar_lista(lista_preguntas):
    random.shuffle(lista_preguntas)