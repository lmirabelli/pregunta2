
import pygame
from menu import *
from juego_original import *
from configuracion import *
from ranking import *
from terminado import agregar_puesto_ranking
from constantes import *
from reglas import *

pygame.init()
reloj = pygame.time.Clock()

ejecutando = True
ventana_actual = "menu"


while ejecutando:
    reloj.tick(30)
    cola_eventos = pygame.event.get()
    
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        ventana_actual = manejar_pantalla_juego(pantalla, cola_eventos)
    elif ventana_actual == "ranking":
        ventana_actual = manejar_pantalla_ranking(pantalla, cola_eventos, "ranking.json")
    elif ventana_actual == "configuraciones":
        ventana_actual = manejar_ajustes_volumen(pantalla, cola_eventos)
    elif ventana_actual == "terminado":
        ventana_actual = agregar_puesto_ranking(pantalla, cola_eventos)
    elif ventana_actual == "reglas":
        ventana_actual = mostrar_reglas(pantalla, cola_eventos)
    elif ventana_actual == "salir":
        ejecutando = False
    
    pygame.display.flip()

pygame.quit()