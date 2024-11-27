import pygame
from constantes import *
from funciones import *

pygame.init()

# Dimensiones deseadas de los botones
# Tamaño deseado para los botones
ancho_boton, alto_boton = 350, 60  
# Espacio vertical entre botones
espaciado = 40  

lista_botones = []

# Crear botones
for i in range(5):
    boton = {}
    boton["superficie"] = pygame.image.load("./img/opcion_default.png")
    boton["superficie"] = pygame.transform.scale(boton["superficie"], (ancho_boton, alto_boton))  # Escalar imagen
    boton["rectangulo"] = boton["superficie"].get_rect()
    lista_botones.append(boton)

def mostrar_menu(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    # Gestionar eventos
    retorno = "menu"
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i, boton in enumerate(lista_botones):
                if boton["rectangulo"].collidepoint(evento.pos):
                    if i == 4:
                        retorno = "salir"
                    elif i == 0:
                        retorno = "juego"
                    elif i == 2:
                        retorno = "ranking"
                    elif i == 1:
                        retorno = "configuraciones"
                    elif i == 3:
                        retorno = "reglas"
        elif evento.type == pygame.QUIT:
            retorno = "salir"
    
    # Dibujar pantalla
    pantalla.blit(fondo_menu, (0, 0))

    # Calcular posiciones centradas para los botones
    for i, boton in enumerate(lista_botones):
        x_centro = (ANCHO - ancho_boton) // 2  # Centrar horizontalmente
        y_pos = (ALTO - (len(lista_botones) * alto_boton + (len(lista_botones) - 1) * espaciado)) // 2 + i * (alto_boton + espaciado)
        boton["rectangulo"].topleft = (x_centro, y_pos)
        pantalla.blit(boton["superficie"], boton["rectangulo"].topleft)
    
    # Dibujar texto en los botones
    texto_con_borde(pantalla,"JUGAR",fuente_menu,BLANCO,NEGRO, (500,140),ancho_borde=3)
    texto_con_borde(pantalla,"CONFIGURACION",fuente_menu,BLANCO,NEGRO, (430,240),ancho_borde=3)
    texto_con_borde(pantalla,"PUNTUACIONES",fuente_menu,BLANCO,NEGRO, (440,340),ancho_borde=3)
    texto_con_borde(pantalla,"REGLAS",fuente_menu,BLANCO,NEGRO, (490,440),ancho_borde=3)
    texto_con_borde(pantalla,"SALIR",fuente_menu,BLANCO,NEGRO, (500,540),ancho_borde=3)
    
    return retorno