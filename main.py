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

jugador_x_cambio = 0

def jugador(x,y):
    # metodo que significa arrojar ,primer dato la imagen , segundo dato es una tupla de x y
    pantalla.blit(img_jugador, (x,y))



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

        # para ver si se presiono alguna tecla, este evento es cuando se presiona la tecla
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_LEFT: #flecha izquierda
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT: #flecha derecha
                jugador_x_cambio = 0.3

        #este evento ocurre cuando se suelta la tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #modificar la ubicacion del jugador
    jugador_x += jugador_x_cambio

    #mantener dentro del borde
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    #llamamos a jugador pa que se actualize constantemente
    jugador(jugador_x,jugador_y)

    # actualizamos la pantalla
    pygame.display.update()








