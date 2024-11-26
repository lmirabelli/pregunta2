import pygame
from constantes import *
from funciones import *

pygame.init()


def manejar_ajustes_volumen(pantalla, cola_eventos):
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            return "salir"
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return "menu"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_subir_volumen_musica.collidepoint(evento.pos):
                # Aumentar el volumen de la música
                volumen_actual = pygame.mixer.music.get_volume()
                if volumen_actual < 1.0:
                    pygame.mixer.music.set_volume(volumen_actual + 0.1)
            elif boton_bajar_volumen_musica.collidepoint(evento.pos):
                # Disminuir el volumen de la música
                volumen_actual = pygame.mixer.music.get_volume()
                if volumen_actual > 0.0:
                    pygame.mixer.music.set_volume(volumen_actual - 0.1)
            elif boton_subir_volumen_sonido.collidepoint(evento.pos):
                # Aumentar el volumen de los efectos de sonido
                ajustar_volumen(sonido_cash, min(sonido_cash.get_volume() + 0.1, 1.0))
                ajustar_volumen(sonido_tambores, min(sonido_tambores.get_volume() + 0.1, 1.0))
                ajustar_volumen(sonido_error, min(sonido_error.get_volume() + 0.1, 1.0))
                ajustar_volumen(sonido_vida, min(sonido_vida.get_volume() + 0.1, 1.0))
            elif boton_bajar_volumen_sonido.collidepoint(evento.pos):
                # Disminuir el volumen de los efectos de sonido
                ajustar_volumen(sonido_cash, max(sonido_cash.get_volume() - 0.1, 0.0))
                ajustar_volumen(sonido_tambores, max(sonido_tambores.get_volume() - 0.1, 0.0))
                ajustar_volumen(sonido_error, max(sonido_error.get_volume() - 0.1, 0.0))
                ajustar_volumen(sonido_vida, max(sonido_vida.get_volume() - 0.1, 0.0))
            elif boton_volver_menu_rect.collidepoint(evento.pos):
                return "menu"

    pantalla.blit(fondo_configuracion, (0, 0))
    mostrar_texto(pantalla, "AJUSTES DE VOLUMENES", (ANCHO//2, 70), fuente_grande, BLANCO)
    dibujar_botones_volumen(pantalla)
    dibujar_boton_volver_menu(pantalla)
    # Dibujar las barras de volumen
    dibujar_barra_volumen(pantalla, 350, 320, pygame.mixer.music.get_volume())
    dibujar_barra_volumen(pantalla, 350, 570, sonido_cash.get_volume())
    
    return "configuraciones"

    pygame.quit()
