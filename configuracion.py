import pygame
from constantes import *
pygame.init()

AZUL = (0, 0, 75)
BLANCO = (245, 245, 245)
NEGRO = (18, 18, 18)

# Cargar imagen de fondo para los botones
imagen_boton = pygame.image.load("./img/opcion_default.png")
imagen_boton = pygame.transform.scale(imagen_boton, (350, 50))
imagen_volver_menu = pygame.image.load("./img/opcion_correcta.png")
imagen_volver_menu = pygame.transform.scale(imagen_volver_menu, (350, 50))

# Botones de volumen
boton_volumen_musica = pygame.Rect(300, 250, 350, 50)
boton_volumen_sonido = pygame.Rect(300, 500, 350, 50)
boton_subir_volumen_musica = pygame.Rect(600, 250, 50, 50)
boton_bajar_volumen_musica = pygame.Rect(300, 250, 50, 50)
boton_subir_volumen_sonido = pygame.Rect(600, 500, 50, 50)
boton_bajar_volumen_sonido = pygame.Rect(300, 500, 50, 50)

# Botón para volver al menú principal
boton_volver_menu = pygame.Rect(365, 650, 350, 50)

def ajustar_volumen(sonido, volumen):
    sonido.set_volume(volumen)

def dibujar_botones_volumen():
    # Dibujar imagen de fondo para botones de volumen música
    pantalla.blit(imagen_boton, (300, 250))
    mostrar_texto(pantalla, "-", (boton_bajar_volumen_musica.centerx, boton_bajar_volumen_musica.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "+", (boton_subir_volumen_musica.centerx, boton_subir_volumen_musica.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "VOLUMEN MUSICA", (boton_volumen_musica.centerx, boton_volumen_musica.centery), fuente, BLANCO)

    # Dibujar imagen de fondo para botones de volumen sonido
    pantalla.blit(imagen_boton, (300, 500))
    mostrar_texto(pantalla, "-", (boton_bajar_volumen_sonido.centerx, boton_bajar_volumen_sonido.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "+", (boton_subir_volumen_sonido.centerx, boton_subir_volumen_sonido.centery), fuente_pequeña, BLANCO)
    mostrar_texto(pantalla, "VOLUMEN SONIDO", (boton_volumen_sonido.centerx, boton_volumen_sonido.centery), fuente, BLANCO)

def dibujar_boton_volver_menu():
    pantalla.blit(imagen_volver_menu, boton_volver_menu.topleft)
    mostrar_texto(pantalla, "VOLVER AL MENU PRINCIPAL", (boton_volver_menu.centerx, boton_volver_menu.centery), fuente, BLANCO)

def mostrar_texto(superficie, texto, posicion, fuente, color):
    texto_superficie = fuente.render(texto, True, color)
    rect_texto = texto_superficie.get_rect(center=posicion)
    superficie.blit(texto_superficie, rect_texto.topleft)

def dibujar_barra_volumen(x, y, volumen):
    for i in range(10):
        color = BLANCO if i < volumen * 10 else AZUL
        pygame.draw.rect(pantalla, color, (x + i * 20, y, 18, 30))

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False  # Cerrar ajustes de volúmenes y volver al menú principal
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
            elif boton_volver_menu.collidepoint(evento.pos):
                ejecutando = False  # Cerrar ajustes de volúmenes y volver al menú principal

    pantalla.blit(fondo_configuracion, (0, 0))
    mostrar_texto(pantalla, "AJUSTES DE VOLUMENES", (ANCHO//2, 70), fuente_grande, BLANCO)
    dibujar_botones_volumen()
    dibujar_boton_volver_menu()
    # Dibujar las barras de volumen
    dibujar_barra_volumen(350, 320, pygame.mixer.music.get_volume())
    dibujar_barra_volumen(350, 570, sonido_cash.get_volume())
    
    pygame.display.flip()

pygame.quit()
