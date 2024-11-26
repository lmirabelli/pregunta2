import pygame
from constantes import *
from funciones import *

pygame.init()

fondo_regla = pygame.image.load("./img/opcion_default.png")  # Cambia a la ruta de tu imagen
fondo_regla = pygame.transform.scale(fondo_regla, (800, 40))


# Función para manejar la pantalla de reglas
def mostrar_reglas(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    # Dibujar fondo
    pantalla.blit(fondo_menu, (0,0))

    # Dibujar texto dentro del rectángulo
    texto = fuente.render("El puntaje de respuesta correcta es el tiempo restante", True, BLANCO)
    pantalla.blit(fondo_regla, (100,100))
    pantalla.blit(texto, (120,108))

    texto = fuente.render("El puntaje de respuesta incorrecta es de -25 puntos", True, BLANCO)
    pantalla.blit(fondo_regla, (100,150))
    pantalla.blit(texto, (120,158))

    texto = fuente.render("La respuesta correcta en bonus vale el tiempo restante x 10", True, BLANCO)
    pantalla.blit(fondo_regla, (100,200))
    pantalla.blit(texto, (120,208))

    texto = fuente.render("El boton pasar pregunta es para saltear la pregunta sin perder vidas", True, BLANCO)
    pantalla.blit(fondo_regla, (100,250))
    pantalla.blit(texto, (120,258))
    
    # Manejar eventos y retorno
    retorno = "reglas"
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            retorno = "menu"


    pygame.display.flip()
    return retorno
