'''
los eventos son todo lo que ocurra dentro de la pantalla de pygame todo lo que haga
tenemos que programar eventos

display se refiere a lo que nosotros veremos o mostramos

'''
import pygame
import random
import math
from pygame import mixer

import io





#para convertir strign a bytes
def fuente_bytes(fuente):
    with open(fuente, 'rb') as f:
        ttf_bytes = f.read()

    return io.BytesIO(ttf_bytes)

#############################################################

pygame.init()

#establecemos el modo en que se muestra pygame (tupla para el ancho y alto)
#creamos una pantalla con valores x,y
pantalla = pygame.display.set_mode((800, 600))

#Editamos el Titulo e Icono del juego
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

#llamamos a la imagen
fondo = pygame.image.load("Fondo.jpg")


#Agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)   #volumen de la musica
mixer.music.play(-1)



#################################################################################################

#Agregamos al personaje del juego
img_jugador = pygame.image.load("cohete.png")
#posision x
jugador_x = 368
#posision y
jugador_y = 500
jugador_x_cambio = 0

#Agregamos al enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []

cantidad_enemigos = 8

for e in range(cantidad_enemigos):

    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))

    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)



#variables de la bala de la nabe
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500

bala_x_cambio = 0  #no la usaremos
bala_y_cambio = 1

bala_visible = False

#variable de puntaje
puntaje = 0

#unico tipo de fuente incorporado con pygame
fuente_como_bytes = fuente_bytes("FreeSansBold.ttf")

fuente = pygame.font.Font(fuente_como_bytes, 32)
texto_x = 10
texto_y = 10


#texto final del juego
fuente_como_bytes_flicker = fuente_bytes("Flicker.ttf")
fuente_final = pygame.font.Font(fuente_como_bytes_flicker, 60)




###########################################################################################

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (200, 200))



#funcion mostrar puntaje desde la fuente es diferente
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


def jugador(x,y):
    # metodo que significa arrojar ,primer dato la imagen , segundo dato es una tupla de x y
    pantalla.blit(img_jugador, (x, y))


def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

#funcion disparar bala
def disparar_bala(x, y):
    # con esto podemos editar el valor de la bala
    global bala_visible
    bala_visible = True

    pantalla.blit(img_bala, (x + 16, y + 10))


#  funcion para detectar las colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia =math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False




#########################################################################

#con esto hacemos que la pantalla permanesca abierta y que escuche todos los eventos
#y se cierre cuando se lo ordenemos
se_ejecuta = True

while se_ejecuta:

    # fill = relleno convinacion de colores RGB(red ,green , blue) tupla ,esta orden necesita que se actualize la pantalla
    #lo pondremos al comienzo pa que la pantalla no tape a nadie
    #pantalla.fill((205, 144, 228))

    #imagen de fondo (ocupa toda la pantalla)
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():#Trae todos los eventos que tiene pygame
        if evento.type == pygame.QUIT:#este evento es el que corresponde a la X de salir
            se_ejecuta = False

        # para ver si se presiono alguna tecla, este evento es cuando se presiona la tecla
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_LEFT: #flecha izquierda
                jugador_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT: #flecha derecha
                jugador_x_cambio = 0.5

            #evento al presionar spacio o disparar
            if evento.key == pygame.K_SPACE:
                #sonido en pygame
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_visible:         #solo lanzara balas cuando sea falsp (visiible == False)
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)


        #este evento ocurre cuando se suelta la tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

#############################################################################################
    #modificar la ubicacion del jugador
    jugador_x += jugador_x_cambio

    #mantener dentro del borde al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736


    # modificar la ubicacion del enemigo
    for e in range(cantidad_enemigos):

        #fin del juego(colision del enemigo con el jugador)
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

    # mantener dentro del borde al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]

        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]

        # llamamos a colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)


        enemigo(enemigo_x[e], enemigo_y[e], e)



    #moviento bala jugador:
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False


    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio




    #llamamos a jugador pa que se actualize constantemente
    jugador(jugador_x, jugador_y)


    mostrar_puntaje(texto_x, texto_y)



    # actualizamos la pantalla
    pygame.display.update()








