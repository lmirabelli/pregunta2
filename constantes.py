import pygame

# Configuración de la pantalla
ANCHO, ALTO = 1080, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Who Wants to Be Millionaire - Equipo del canal cultural!!!")
icono = pygame.image.load("./img/icono.png")
pygame.display.set_icon(icono)



# Colores
NEGRO = (18, 18, 18)
BLANCO = (245, 245, 245)


# Fuente para mostrar texto
pygame.init()
fuente = pygame.font.Font(None, 28)
fuente_grande = pygame.font.Font(None, 60)
fuente_pequeña = pygame.font.Font(None, 40)

# Sonidos
sonido_cash = pygame.mixer.Sound("./sound/cash_sound.mp3")
sonido_cash.set_volume(1)
sonido_tambores = pygame.mixer.Sound("./sound/tambores.mp3")
sonido_tambores.set_volume(0.2)
sonido_error = pygame.mixer.Sound("./sound/sonido_error.mp3")
sonido_error.set_volume(0.2)

#MUSICA
pygame.mixer.init()
pygame.mixer.music.load("./sound/musica.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

# Fondos de pantalla
fondo = pygame.image.load("./img/fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
fondo_pregunta = pygame.image.load("./img/fondo_pregunta.png")
fondo_pregunta = pygame.transform.scale(fondo_pregunta, (650, 100))  # Ajustar tamaño
fondo_ranking = pygame.image.load("./img/fondo_ranking.png")
fondo_ranking = pygame.transform.scale(fondo_ranking, (ANCHO, ALTO))
imagen_opcion_default = pygame.image.load("./img/opcion_default.png")
imagen_opcion_correcta = pygame.image.load("./img/opcion_correcta.png")
imagen_opcion_incorrecta = pygame.image.load("./img/opcion_incorrecta.png")
imagen_opcion_default = pygame.transform.scale(imagen_opcion_default, (600, 50))
imagen_opcion_correcta = pygame.transform.scale(imagen_opcion_correcta, (600, 50))
imagen_opcion_incorrecta = pygame.transform.scale(imagen_opcion_incorrecta, (600, 50))