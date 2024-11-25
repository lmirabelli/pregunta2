import pygame
from constantes import *
from funciones import *

pygame.init()
fuente_menu = pygame.font.SysFont("Arial Narrow",30)
lista_botones = []

for i in range(4):
    boton = {}
    boton["superficie"] = imagen_opcion_default  # Usar la imagen escalada
    boton["rectangulo"] = boton["superficie"].get_rect(topleft=(220, 350 + i * 100))  # Posicionar los botones
    lista_botones.append(boton)


def mostrar_menu(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    # Gestionar eventos:
    retorno = "menu"
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i, boton in enumerate(lista_botones): 
                if boton["rectangulo"].collidepoint(evento.pos):
                    # CLICK_SONIDO.play()
                    if i == 3:
                        retorno = "salir"  
                    elif i == 0:
                        retorno = "juego"  
                    elif i == 2:
                        retorno = "rankings"
                    elif i == 1:
                        retorno = "configuraciones"        
        elif evento.type == pygame.QUIT:
            retorno = "salir"
                
    # Dibujar pantalla y las otras superficies
    pantalla.blit(fondo_ranking, (0, 0))
    
    for i, boton in enumerate(lista_botones):
        y_pos = 115 + i * 80  # Posición dinámica para cada botón
        boton["rectangulo"] = pantalla.blit(boton["superficie"], (125, y_pos))
    
    mostrar_texto_menu(lista_botones[0]["superficie"], "JUGAR", (80, 10), fuente_menu, BLANCO)
    mostrar_texto_menu(lista_botones[1]["superficie"], "CONFIGURACION", (20, 10), fuente_menu, BLANCO)
    mostrar_texto_menu(lista_botones[2]["superficie"], "PUNTUACIONES", (25, 10), fuente_menu, BLANCO)
    mostrar_texto_menu(lista_botones[3]["superficie"], "SALIR", (80, 10), fuente_menu, BLANCO)
    
    return retorno
