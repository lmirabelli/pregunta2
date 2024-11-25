# principal.py
import pygame
from menu import *
from juego_original import *
# from configuracion import *
from ranking import *
from constantes import *

pygame.init()
reloj = pygame.time.Clock()

def main():
    ejecutando = True
    estado_actual = "menu"
    
    while ejecutando:
        reloj.tick(30)
        eventos = pygame.event.get()
        
        if estado_actual == "menu":
            estado_actual = mostrar_menu(pantalla, eventos)
        elif estado_actual == "juego":
            estado_actual = juego_trivia(pantalla, fondo, fondo_pregunta, fuente, fuente_grande, imagen_opcion_default, imagen_opcion_correcta, imagen_opcion_incorrecta, sonido_tambores, sonido_cash, sonido_error, sonido_vida)
        # elif estado_actual == "configuraciones":
        #     mostrar_configuracion(pantalla)
        #     estado_actual = "menu"
        elif estado_actual == "rankings":
            pantalla_ranking(pantalla, "ranking.json")
            estado_actual = "menu"
        elif estado_actual == "salir":
            ejecutando = False
    
    pygame.quit()

if __name__ == "__main__":
    main()