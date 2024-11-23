import json
import pygame
from constantes import *



# Cargar datos del ranking desde un archivo JSON
def cargar_ranking(archivo):
        with open(archivo, "r", encoding="utf-8") as file:
            return json.load(file)
        return []

# Ordenar el ranking por puntos de mayor a menor
def obtener_top_10(ranking):
    return sorted(ranking, key=lambda x: x["puntos"], reverse=True)[:10]

# Mostrar ranking en pantalla
def mostrar_ranking(pantalla, top_10):
    pantalla.blit(fondo_ranking, (0, 0))

    # Listar los jugadores y puntos
    y_offset = 50
    tamano_fuente_dinamica = 35
    for index, jugador in enumerate(top_10):
        fuente_dinamica = pygame.font.Font(None, tamano_fuente_dinamica)
        texto = f"{index + 1}. {jugador['jugador']}:  {jugador['puntos']} puntos"
        texto_render = fuente_dinamica.render(texto, True, BLANCO)

        # Dimensiones del texto para posicionar la imagen de fondo
        tamano_fuente_dinamica = tamano_fuente_dinamica - 2
        rect = texto_render.get_rect()
        rect.height = texto_render.get_height() + 12
        rect.width = texto_render.get_width() + 20
        posicion_x = (ANCHO - rect.width) // 2
        rect.topleft = (posicion_x, y_offset)

        # Escalar la imagen de fondo al tamaño del rectángulo
        imagen_fondo_escalada = pygame.transform.scale(imagen_opcion_default, (rect.width + 20, rect.height + 20))

        # Dibujar la imagen de fondo
        pantalla.blit(imagen_fondo_escalada, (rect.x - 10, rect.y - 10))

        # Dibujar el texto sobre la imagen
        texto_pos_x = rect.x + 10  # Margen horizontal para el texto
        texto_pos_y = rect.y + (rect.height - texto_render.get_height()) // 2  # Centramos verticalmente
        pantalla.blit(texto_render, (texto_pos_x, texto_pos_y))
        y_offset += rect.height + 30  # Espaciado adicional entre filas

    # Fondo para el mensaje
    mensaje = fuente.render("Presiona ESC para regresar al menú", True, BLANCO)
    mensaje_rect = mensaje.get_rect(center=(ANCHO // 2, ALTO - 50))

    # Escalar y dibujar el fondo para el mensaje
    fondo_mensaje = pygame.transform.scale(imagen_opcion_incorrecta, (mensaje_rect.width + 20, mensaje_rect.height + 10))
    pantalla.blit(fondo_mensaje, (mensaje_rect.x - 10, mensaje_rect.y - 5))

    # Dibujar el texto del mensaje
    pantalla.blit(mensaje, mensaje_rect)

# Función principal para manejar la pantalla del ranking
def pantalla_ranking(pantalla, archivo_ranking):
    ranking = cargar_ranking(archivo_ranking)
    top_10 = obtener_top_10(ranking)

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                ejecutando = False

        mostrar_ranking(pantalla, top_10)
        pygame.display.flip()

# Prueba de la funcionalidad
if __name__ == "__main__":
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Ranking")
    archivo_ranking = "ranking.json"
    pantalla_ranking(pantalla, archivo_ranking)
