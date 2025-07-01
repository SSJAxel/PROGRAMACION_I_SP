import pygame
import random

def crear_tablero(filas, columnas):
    return [[0 for _ in range(columnas)] for _ in range(filas)]

def puede_colocar(tablero, fila, columna, tamaño, horizontal=True):
    filas = len(tablero)
    columnas = len(tablero[0])
    for i in range(tamaño):
        f = fila + (i if not horizontal else 0)
        c = columna + (i if horizontal else 0)
        for df in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nf, nc = f + df, c + dc
                if 0 <= nf < filas and 0 <= nc < columnas:
                    if tablero[nf][nc] != 0:
                        return False
    if horizontal:
        if columna + tamaño > columnas:
            return False
    else:
        if fila + tamaño > filas:
            return False
    return True

def colocar_barcos_juego(tablero, barcos):
    filas = len(tablero)
    columnas = len(tablero[0])
    for tamaño, cantidad in barcos:
        for _ in range(cantidad):
            colocado = False
            intentos = 0
            while not colocado and intentos < 1000:
                horizontal = random.choice([True, False])
                if horizontal:
                    fila = random.randint(0, filas - 1)
                    columna = random.randint(0, columnas - tamaño)
                else:
                    fila = random.randint(0, filas - tamaño)
                    columna = random.randint(0, columnas - 1)
                if puede_colocar(tablero, fila, columna, tamaño, horizontal):
                    for i in range(tamaño):
                        if horizontal:
                            tablero[fila][columna + i] = 1
                        else:
                            tablero[fila + i][columna] = 1
                    colocado = True
                intentos += 1
            if not colocado:
                return False
    return True

def dibujar_tablero(superficie, tablero, offset_x, offset_y, tam_casilla, colores, mostrar_barcos=False):
    filas = len(tablero)
    columnas = len(tablero[0])
    for fila in range(filas):
        for col in range(columnas):
            rect = pygame.Rect(
                offset_x + col * tam_casilla,
                offset_y + fila * tam_casilla,
                tam_casilla, tam_casilla
            )
            if tablero[fila][col] == 2:
                pygame.draw.rect(superficie, colores['ROJO'], rect)
            elif tablero[fila][col] == 3:
                pygame.draw.rect(superficie, colores['NEGRO'], rect)
            elif tablero[fila][col] == 1 and mostrar_barcos:
                pygame.draw.rect(superficie, colores['AZUL'], rect)
            pygame.draw.rect(superficie, colores['GRIS'], rect, 2)

def todos_los_barcos_hundidos(tablero):
    for fila in tablero:
        if 1 in fila:
            return False
    return True

def contar_nave(tablero, fila, col):
    tamaño = 1
    columnas = len(tablero[0])
    filas = len(tablero)
    c = col - 1
    while c >= 0 and tablero[fila][c] in [1,2]:
        tamaño += 1
        c -= 1
    c = col + 1
    while c < columnas and tablero[fila][c] in [1,2]:
        tamaño += 1
        c += 1
    f = fila - 1
    while f >= 0 and tablero[f][col] in [1,2]:
        tamaño += 1
        f -= 1
    f = fila + 1
    while f < filas and tablero[f][col] in [1,2]:
        tamaño += 1
        f += 1
    return tamaño

def nave_hundida(tablero, fila, col):
    filas = len(tablero)
    columnas = len(tablero[0])
    for df, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        f, c = fila, col
        while 0 <= f < filas and 0 <= c < columnas and tablero[f][c] != 0 and tablero[f][c] != 3:
            if tablero[f][c] == 1:
                return False
            f += df
            c += dc
    return True
