'''
los eventos son todo lo que ocurra dentro de la pantalla de pygame todo lo que haga
tenemos que programar eventos

display se refiere a lo que nosotros veremos o mostramos

'''
import pygame



#############################################################

pygame.init()

#establecemos el modo en que se muestra pygame (tupla para el ancho y alto)
#creamos una pantalla con valores x,y
pantalla = pygame.display.set_mode((800, 600))

#Editamos el Titulo e Icono del juego
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

#################################################################################################

#Agregamos al personaje del juego
img_jugador = pygame.image.load("cohete.png")

#posision x
jugador_x = 368

#posision y
jugador_y = 536
def jugador():
    # metodo que significa arrojar ,primer dato la imagen , segundo dato es una tupla de x y
    pantalla.blit(img_jugador, (jugador_x,jugador_y))



###############################################################################################3

#con esto hacemos que la pantalla permanesca abierta y que escuche todos los eventos
#y se cierre cuando se lo ordenemos
se_ejecuta = True

while se_ejecuta:

    # fill = relleno convinacion de colores RGB(red ,green , blue) tupla ,esta orden necesita que se actualize la pantalla
    #lo pondremos al comienzo pa que la pantalla no tape a nadie
    pantalla.fill((205, 144, 228))

    for evento in pygame.event.get():#Trae todos los eventos que tiene pygame
        if evento.type == pygame.QUIT:#este evento es el que corresponde a la X de salir
            se_ejecuta = False

    #llamamos a jugador pa que se actualize constantemente
    jugador()

    # actualizamos la pantalla
    pygame.display.update()








