# Tamaño de la ventana
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

# Colores (R, G, B)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 120, 255)
ROJO = (255, 0, 0)
GRIS = (200, 200, 200)

COLUMNAS = 10
FILAS = 10

TAM_CASILLA = min(
    (ANCHO_VENTANA - 120) // COLUMNAS,  # 60px de margen a cada lado
    (ALTO_VENTANA - 120) // FILAS       # 60px arriba y abajo
)

