from clases import *
import pygame

Controlador.iniciar()

colores = {"Blanco": (255, 255, 255), "Negro": (0, 0, 0)}

ancho = 1280
alto = 720

fps = 120

fondo = Fondo()

ventana = Controlador.configurar_pantalla(ancho, alto)

reloj = Controlador.iniciar_reloj()

Controlador.Inicializar_Titulo()
Controlador.Inicializar_Subtitulo()

frames_totales = 0

delay = 10

frame = frames_totales

pygame.mixer.music.load("menu_principal.wav")

pygame.mixer.music.play(2,0)
pygame.mixer.music.set_volume(0.25)

while True:

    Controlador.set_fps(reloj, fps)
    Controlador.buscar_eventos()

    Controlador.mover()

    if frame + delay < frames_totales:
        if len(Base.letras_pasivas) > 0:
            frame = Controlador.proxima_letra(frames_totales)

    Dibujo.dibujo(fondo, ventana, colores)

    delay += 5

    if delay == 15:
        delay = 5

    frames_totales += 1
