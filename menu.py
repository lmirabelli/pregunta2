import pygame
from constantes import *
from funciones import *

pygame.init()

lista_botones = []

for i in range(4):
    boton = {}
    boton["superficie"] = pygame.image.load("./img/opcion_default.png")
    boton["superficie"] = pygame.transform.scale(boton["superficie"], (600, 50))
    boton["rectangulo"] = boton["superficie"].get_rect()
    lista_botones.append(boton)

def mostrar_menu(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    # Gestionar eventos:
    retorno = "menu"
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i, boton in enumerate(lista_botones):
                if boton["rectangulo"].collidepoint(evento.pos):
                    if i == 3:
                        retorno = "salir"
                    elif i == 0:
                        retorno = "juego"
                    elif i == 2:
                        retorno = "ranking"
                    elif i == 1:
                        retorno = "configuraciones"
        elif evento.type == pygame.QUIT:
            retorno = "salir"
                
    # Dibujar pantalla 
    pantalla.blit(fondo_menu, (0, 0))
    
    lista_botones[0]["rectangulo"].topleft = (125, 130)
    lista_botones[1]["rectangulo"].topleft = (145, 210)
    lista_botones[2]["rectangulo"].topleft = (165, 290)
    lista_botones[3]["rectangulo"].topleft = (185, 370)
    
    pantalla.blit(lista_botones[0]["superficie"], lista_botones[0]["rectangulo"].topleft)
    pantalla.blit(lista_botones[1]["superficie"], lista_botones[1]["rectangulo"].topleft)
    pantalla.blit(lista_botones[2]["superficie"], lista_botones[2]["rectangulo"].topleft)
    pantalla.blit(lista_botones[3]["superficie"], lista_botones[3]["rectangulo"].topleft)
    
    mostrar_texto_menu(lista_botones[0]["superficie"], "JUGAR", (35, 15), fuente_menu, BLANCO)
    mostrar_texto_menu(lista_botones[1]["superficie"], "CONFIGURACION", (35, 15), fuente_menu, BLANCO)
    mostrar_texto_menu(lista_botones[2]["superficie"], "PUNTUACIONES", (35, 15), fuente_menu, BLANCO)
    mostrar_texto_menu(lista_botones[3]["superficie"], "SALIR", (35, 15), fuente_menu, BLANCO)
    
    return retorno
