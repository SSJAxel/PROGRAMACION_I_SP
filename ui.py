import pygame
import sys

def dibujar_boton_menu(superficie, texto, rect, fuente, activo=False):
    color_base = (30, 60, 90, 180)
    color_hover = (60, 100, 140, 220)
    color = color_hover if activo else color_base
    boton_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    pygame.draw.rect(boton_surface, color, boton_surface.get_rect(), border_radius=18)
    pygame.draw.rect(boton_surface, (255, 255, 255, 120), boton_surface.get_rect(), 3, border_radius=18)
    superficie.blit(boton_surface, rect.topleft)
    texto_render = fuente.render(texto, True, (230, 230, 230))
    texto_rect = texto_render.get_rect(center=rect.center)
    superficie.blit(texto_render, texto_rect)

def pedir_nombre_pygame(ventana, fuente, mar_scaled, offset_x_mar, offset_y_mar, ANCHO_VENTANA, ALTO_VENTANA):
    nombre = ""
    input_box = pygame.Rect(ANCHO_VENTANA//2 - 200, ALTO_VENTANA//2, 400, 60)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    if nombre.strip() == "":
                        nombre = "Jugador"
                    return nombre
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    if len(nombre) < 16 and evento.unicode.isprintable():
                        nombre += evento.unicode
        ventana.blit(mar_scaled, (offset_x_mar, offset_y_mar))
        overlay = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA), pygame.SRCALPHA)
        overlay.fill((0,0,0,180))
        ventana.blit(overlay, (0,0))
        texto = fuente.render("Ingresa tu nombre:", True, (255,255,255))
        ventana.blit(texto, (ANCHO_VENTANA//2 - texto.get_width()//2, ALTO_VENTANA//2 - 80))
        pygame.draw.rect(ventana, (255,255,255), input_box, 2)
        texto_nombre = fuente.render(nombre, True, (255,255,255))
        ventana.blit(texto_nombre, (input_box.x+10, input_box.y+10))
        pygame.display.flip()
    return nombre

def mostrar_puntajes(ventana, fondo_mar_scaled, offset_x, ALTO_VENTANA, ANCHO_VENTANA, FUENTE_GRIEGA):
    fuente = pygame.font.SysFont(FUENTE_GRIEGA, 40, bold=True)
    ventana.blit(fondo_mar_scaled, (offset_x, 0))
    try:
        with open("puntajes.txt", "r", encoding="utf-8") as f:
            puntajes = [line.strip().split(',') for line in f if ',' in line]
            puntajes = sorted(puntajes, key=lambda x: int(x[1]), reverse=True)[:3]
    except Exception:
        puntajes = []
    titulo = fuente.render("Mejores Puntajes", True, (255,255,255))
    ventana.blit(titulo, (ANCHO_VENTANA//2 - titulo.get_width()//2, 100))
    fuente2 = pygame.font.SysFont(FUENTE_GRIEGA, 32)
    for i, (nombre, puntaje) in enumerate(puntajes):
        texto = fuente2.render(f"{i+1}. {nombre} - {int(puntaje):04d}", True, (255,255,255))
        ventana.blit(texto, (ANCHO_VENTANA//2 - 200, 180 + i*40))
    texto_volver = fuente2.render("[Click para volver]", True, (200,200,200))
    ventana.blit(texto_volver, (ANCHO_VENTANA//2 - 120, ALTO_VENTANA - 80))
    pygame.display.flip()
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                esperando = False
