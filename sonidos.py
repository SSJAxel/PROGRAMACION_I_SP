
import pygame

def cargar_sonidos():
    try:
        pygame.mixer.music.load("tribe-drum-loop-103173.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except Exception as e:
        print("No se pudo cargar la música de fondo:", e)
    try:
        sonido_disparo = pygame.mixer.Sound("single-pistol-gunshot-33-37187.mp3")
        sonido_disparo.set_volume(0.10)
    except Exception as e:
        print("No se pudo cargar el sonido de disparo:", e)
        sonido_disparo = None
    return sonido_disparo

def mutear_musica(muteado):
    pygame.mixer.music.set_volume(0 if muteado else 0.5)

import pygame

def cargar_sonidos():
    try:
        pygame.mixer.music.load("tribe-drum-loop-103173.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except Exception as e:
        print("No se pudo cargar la música de fondo:", e)
    try:
        sonido_disparo = pygame.mixer.Sound("single-pistol-gunshot-33-37187.mp3")
        sonido_disparo.set_volume(0.10)
    except Exception as e:
        print("No se pudo cargar el sonido de disparo:", e)
        sonido_disparo = None
    return sonido_disparo

def mutear_musica(muteado):
    pygame.mixer.music.set_volume(0 if muteado else 0.5)

