'''
los eventos son todo lo que ocurra dentro de la pantalla de pygame todo lo que haga
tenemos que programar eventos
'''
import pygame



#############################################################

pygame.init()

#establecemos el modo en que se muestra pygame (tupla para el alto y ancho)
#creamos una pantalla con valores y,x
pantalla = pygame.display.set_mode((800, 600))


#con esto hacemos que la pantalla permanesca abierta y que escuche todos los eventos
#y se cierre cuando se lo ordenemos
se_ejecuta = True

while se_ejecuta:
    for evento in pygame.event.get():#Trae todos los eventos que tiene pygame
        if evento.type == pygame.QUIT:#este evento es el que corresponde a la X de salir
            se_ejecuta = False

##################################################################################3






