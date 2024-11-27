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
ROJO = (255, 0, 0)


# FUENTES
pygame.init()
fuente = pygame.font.SysFont("Yusei Magic Regular", 20)
fuente_grande_configuraciones = pygame.font.SysFont("IM FELL ENGLISH SC", 30)
fuente_juego = pygame.font.SysFont("Poetsen One", 30)
fuente_grande = pygame.font.SysFont("Cinzel", 60)
fuente_pequeña = pygame.font.SysFont("Cinzel", 25)
fuente_menu = pygame.font.SysFont("Tilt Warp Regular", 30)
fuente_preguntas = pygame.font.SysFont ("Poetsen One", 20)
fuente_respuestas = pygame.font.SysFont ("Poetsen One", 20)
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

#LO DE ABAJO ES DEL MODULO CONFIGURACIONES
imagen_boton = pygame.image.load("./img/opcion_default.png")
imagen_boton = pygame.transform.scale(imagen_boton, (350, 50))
imagen_volver_menu = pygame.image.load("./img/opcion_correcta.png")
imagen_volver_menu = pygame.transform.scale(imagen_volver_menu, (480,50))
boton_volumen_musica = pygame.Rect(350, 250, 350, 50)
boton_volumen_sonido = pygame.Rect(350, 500, 350, 50)
boton_subir_volumen_musica = pygame.Rect(650, 250, 50, 50)
boton_bajar_volumen_musica = pygame.Rect(335, 250, 50, 50)
boton_subir_volumen_sonido = pygame.Rect(650, 500, 50, 50)
boton_bajar_volumen_sonido = pygame.Rect(335, 500, 50, 50)
boton_volver_menu_rect = pygame.Rect(280, 650, 350, 50)

#MUSICA
pygame.mixer.init()
pygame.mixer.music.load("./sound/musica.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

# BACKGROUNDS

fondo = pygame.image.load("./img/fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
fondo_pregunta = pygame.image.load("./img/fondo_pregunta.png")
fondo_pregunta = pygame.transform.scale(fondo_pregunta, (850, 100)) 
fondo_ranking = pygame.image.load("./img/fondo_ranking.png")
fondo_ranking = pygame.transform.scale(fondo_ranking, (ANCHO, ALTO))
fondo_configuracion = pygame.image.load("img/fondo_configuraciones.png")
fondo_configuracion = pygame.transform.scale(fondo_configuracion, (ANCHO,ALTO))
imagen_opcion_default = pygame.image.load("./img/opcion_default.png")
imagen_opcion_correcta = pygame.image.load("./img/opcion_correcta.png")
imagen_opcion_incorrecta = pygame.image.load("./img/opcion_incorrecta.png")
imagen_opcion_default = pygame.transform.scale(imagen_opcion_default, (600, 50))
imagen_opcion_correcta = pygame.transform.scale(imagen_opcion_correcta, (600, 50))
imagen_opcion_incorrecta = pygame.transform.scale(imagen_opcion_incorrecta, (600, 50))
imagen_boton_skip_default = pygame.image.load("./img/opcion_default.png")
imagen_boton_skip_default = pygame.transform.scale(imagen_boton_skip_default, (250, 50))
imagen_boton_skip_incorrecta = pygame.image.load("./img/opcion_incorrecta.png")
imagen_boton_skip_incorrecta = pygame.transform.scale(imagen_boton_skip_incorrecta, (250, 50))
fondo_menu = pygame.image.load("./img/fondo_ranking.png")
fondo_menu = pygame.transform.scale(fondo, (ANCHO, ALTO))
fondo_bonus = pygame.image.load("img/fondo_bonus.png")
fondo_bonus = pygame.transform.scale(fondo_bonus, (ANCHO, ALTO))
fondo_menu_regla = pygame.image.load("img/fondo_reglas.png")
fondo_menu_regla = pygame.transform.scale(fondo_menu_regla, (1080,720))
fondo_regla = pygame.image.load("./img/opcion_default.png")  # Cambia a la ruta de tu imagen
fondo_regla = pygame.transform.scale(fondo_regla, (800, 40))