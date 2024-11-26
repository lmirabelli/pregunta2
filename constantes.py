import pygame



# PANTALLA
ANCHO, ALTO = 1080, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("QUIEN QUIERE SER MILLONARIO - Equipo del canal cultural!!!")
icono = pygame.image.load("./img/icono.png")
pygame.display.set_icon(icono)



# COLORES
NEGRO = (18, 18, 18)
BLANCO = (245, 245, 245)
AZUL = (0, 0, 75)


# FUENTES
pygame.init()
fuente = pygame.font.Font(None, 28)
fuente_grande = pygame.font.Font(None, 60)
fuente_pequeña = pygame.font.Font(None, 40)
fuente_menu = pygame.font.SysFont("Arial Narrow", 30)
fuente_30 = pygame.font.Font(None, 30)
fuente_25 = pygame.font.Font(None, 25)
fuente_22 = pygame.font.Font(None, 22)
fuente_20 = pygame.font.Font(None, 20)

# SONIDOS
bonus_sound = pygame.mixer.Sound("./sound/bonus_sound.mp3") #PASAR GDB
bonus_sound.set_volume(1)
sonido_cash = pygame.mixer.Sound("./sound/cash_sound.mp3")
sonido_cash.set_volume(1)
sonido_tambores = pygame.mixer.Sound("./sound/tambores.mp3")
sonido_tambores.set_volume(0.2)
sonido_error = pygame.mixer.Sound("./sound/sonido_error.mp3")
sonido_error.set_volume(0.2)
sonido_vida = pygame.mixer.Sound("./sound/sonido_vida.mp3")
sonido_vida.set_volume(0.2)

# BOTONES
boton_skip = pygame.mixer.Sound("./sound/boton_skip.mp3") #PASAR GDB
boton_skip.set_volume(1)
imagen_boton = pygame.image.load("./img/opcion_default.png")
imagen_boton = pygame.transform.scale(imagen_boton, (350, 50))
imagen_volver_menu = pygame.image.load("./img/opcion_correcta.png")
imagen_volver_menu = pygame.transform.scale(imagen_volver_menu, (350, 50))
boton_volumen_musica = pygame.Rect(300, 250, 350, 50)
boton_volumen_sonido = pygame.Rect(300, 500, 350, 50)
boton_subir_volumen_musica = pygame.Rect(600, 250, 50, 50)
boton_bajar_volumen_musica = pygame.Rect(300, 250, 50, 50)
boton_subir_volumen_sonido = pygame.Rect(600, 500, 50, 50)
boton_bajar_volumen_sonido = pygame.Rect(300, 500, 50, 50)
boton_volver_menu_rect = pygame.Rect(365, 650, 350, 50)

#MUSICA
pygame.mixer.init()
pygame.mixer.music.load("./sound/musica.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

# BACKGROUNDS

fondo = pygame.image.load("./img/fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
fondo_pregunta = pygame.image.load("./img/fondo_pregunta.png")
fondo_pregunta = pygame.transform.scale(fondo_pregunta, (650, 100)) 
fondo_ranking = pygame.image.load("./img/fondo_ranking.png")
fondo_ranking = pygame.transform.scale(fondo_ranking, (ANCHO, ALTO))
fondo_configuracion = pygame.transform.scale(icono, (ANCHO, ALTO))
imagen_opcion_default = pygame.image.load("./img/opcion_default.png")
imagen_opcion_correcta = pygame.image.load("./img/opcion_correcta.png")
imagen_opcion_incorrecta = pygame.image.load("./img/opcion_incorrecta.png")
imagen_opcion_default = pygame.transform.scale(imagen_opcion_default, (600, 50))
imagen_opcion_correcta = pygame.transform.scale(imagen_opcion_correcta, (600, 50))
imagen_opcion_incorrecta = pygame.transform.scale(imagen_opcion_incorrecta, (600, 50))
imagen_boton_skip_default = pygame.image.load("./img/opcion_default.png")
imagen_boton_skip_default = pygame.transform.scale(imagen_boton_skip_default, (200, 50))
imagen_boton_skip_incorrecta = pygame.image.load("./img/opcion_incorrecta.png")
imagen_boton_skip_incorrecta = pygame.transform.scale(imagen_boton_skip_incorrecta, (200, 50))
fondo_menu = pygame.image.load("./img/fondo_ranking.png")
fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO, ALTO))