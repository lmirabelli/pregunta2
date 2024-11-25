import pygame
import sys
from constantes import *
from funciones import *

pygame.init()

# Fuente para el texto
fuente = pygame.font.Font(None, 40)

# Cargar imagen del botón
boton_imagen = pygame.image.load("./img/opcion_default.png")
boton_imagen = pygame.transform.scale(boton_imagen, (300, 70))

# Opciones del menú de fin del juego
opciones = ["Reintentar", "Menú Principal", "Salir"]

# Coordenadas y tamaños de las opciones
ancho_opcion = boton_imagen.get_width()
alto_opcion = boton_imagen.get_height()
espaciado = 20
x_opcion = (ANCHO - ancho_opcion) // 2
y_opcion = (ALTO - (alto_opcion * len(opciones) + espaciado * (len(opciones) - 1))) // 2

# Función para mostrar la pantalla de fin del juego
def mostrar_fin_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    print("Estoy en la pantalla de fin del juego")
    retorno = "terminado"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = evento.pos
            for i, opcion in enumerate(opciones):
                x_op = x_opcion
                y_op = y_opcion + i * (alto_opcion + espaciado)
                if x_op <= x_mouse <= x_op + ancho_opcion and y_op <= y_mouse <= y_op + alto_opcion:
                    if opcion == "Reintentar":
                        retorno = "juego"
                    elif opcion == "Menú Principal":
                        retorno = "menu"
                    elif opcion == "Salir":
                        retorno = "salir"
        elif evento.type == pygame.QUIT:
            retorno = "salir"

    pantalla.blit(fondo_ranking, (0, 0))
    texto = fuente.render("Fin del Juego", True, BLANCO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, y_opcion - 100))

    for i, opcion in enumerate(opciones):
        x_op = x_opcion
        y_op = y_opcion + i * (alto_opcion + espaciado)
        pantalla.blit(boton_imagen, (x_op, y_op))
        texto = fuente.render(opcion, True, BLANCO)
        pantalla.blit(texto, (x_op + (ancho_opcion - texto.get_width()) // 2,
                              y_op + (alto_opcion - texto.get_height()) // 2))

    return retorno

if __name__ == "__main__":
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Fin del Juego")
    datos_juego = {"puntuacion": 0, "vidas": 3, "nombre": "", "volumen_musica": 100, "volumen_sonidos": 100}
    mostrar_fin_juego(pantalla, pygame.event.get(), datos_juego)
