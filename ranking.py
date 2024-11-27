import pygame
from constantes import *
from funciones import *

pygame.init()

# Función para manejar la pantalla de rankings
def manejar_pantalla_ranking(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], archivo_ranking: str) -> str:
    # Cargar y procesar datos
    ranking = cargar_ranking(archivo_ranking)
    top_10 = obtener_top_10(ranking)
    
    # Manejar eventos y retorno
    retorno = "ranking"
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            retorno = "menu"
    
    # Dibujar ranking
    mostrar_ranking(pantalla, top_10)
    pygame.display.flip()
    return retorno