

import pygame
import sys
import random
import math
from pygame import mixer
# 1) importamos la libreria pygame
# 2) inicializamos la libreria pygame con .init para traer todos los atributos y herramientas que tiene pygame
pygame.init()
#---------------------------------------------------------------------------------------------------------------------------------------#

# 3) Pantalla
# Creamos nuestra Pantalla de inicio del programa, guardandola en una variable, asignadole los pixeles (height,weight)
pantalla = pygame.display.set_mode((800, 600))
fondo = pygame.image.load("Fondo.jpg")


#---------------------------------------------------------------------------------------------------------------------------------------#
# 4) Titulo
# set_caption --> establece cual va hacer el titulo de la panatalla de nuestra interfaz
pygame.display.set_caption("Juego Espacial")
#---------------------------------------------------------------------------------------------------------------------------------------#

# 5) Icono
# image.load(archivo.png)--> Carga nuestro imagen que queremos poner
icono = pygame.image.load("ovni.png")
# para verlo en nuestra interfaz
# set_icono("imagen.png")--> almacenamos nuestra imagen ya cargada para que aparezca
pygame.display.set_icon(icono)
#---------------------------------------------------------------------------------------------------------------------------------------#
# 6) Creamos nuestro jugador
# Es decir en este caso vamos a cargar nuestra imagen que va a representar nuestro jugador
imgJugador = pygame.image.load("cohete.png")

# 7)Posicion inicial de nuestro jugador
posicionX = 360
posicionY = 500
# 8) Posicion del jugador cuando se opriman las teclas
posicion_en_MovimientoP = 0

#---------------------------------------------------------------------------------------------------------------------------------------#
# 9)Creamos a nuestro Enemigo

imgEnemigo = []
posicionXE = []
posicionYE = []
posicion_en_MovimientoX_E = []
posicion_en_MovimientoY_E = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    imgEnemigo.append(pygame.image.load("enemigo.png"))
    posicionXE.append(random.randint(0, 736))
    posicionYE.append(random.randint(50, 200))
    posicion_en_MovimientoX_E.append(0.3)
    posicion_en_MovimientoY_E.append(50)

# Agregar musica
# cargamos la musica atravez con mixer.music.load()
mixer.music.load('MusicaFondo.mp3')
# para que suene la musica damos play.load(-1) para que suene infinitamente
mixer.music.play(-1)
# ----------------------------------------------------------------------------------------------------------------------------------------------
# FUNCIONES


def jugador(x, y):
    # blit()--> Para indicar que y en que posicion va estar en mi pantalla ( imgJugador, la posicion en el eje x ,posicion en el eje y)
    pantalla.blit(imgJugador, (x, y))


def enemigo(x, y, ene):
    # blit()--> Para indicar que y en que posicion va estar en mi pantalla ( imgJugador, la posicion en el eje x ,posicion en el eje y)
    pantalla.blit(imgEnemigo[ene], (x, y))


def bala(x, y):
    global balaVisible
    balaVisible = True
    pantalla.blit(imgBala, (x+15, y+10))


def detectarColicion(x_1, y_1, x_2, y_2):
    # hacemos la siguiente formula √((x_2-x_1)²+(y_2-y_1)² para hallar la distancia entre dos puntos
    distancia = math.sqrt(math.pow((x_2-x_1), 2)+math.pow((y_2-y_1), 2))
    # si la distancia entre la bala y el enemigo es menor a 27
    if distancia < 27:
        return True
    else:
        return False


def mostrar_puntaje(x, y):
    # render --> nos va a mostrar en pantalla el puntaje , con un color
    texto = fuente.render(f"Puntaje : {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


#---------------------------------------------------------------------------------------------------------------------------------------#
# 12)Posicion inicial de nuestra Bala
imgBala = pygame.image.load('bala.png')
posicionbalaX = 0
posicionbalaY = 500
posicionMovimientoBalaX = 0
posicionMovimientoBalaY = 1
balaVisible = False
# Puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
textoX = 10
texto_y = 10


#---------------------------------------------------------------------------------------------------------------------------------------#

# 12) creamos un bucle while para que se ejecute nuetro programa cada ves que sea True
while True:
    # 13 ) Movimiento del jugador

    # ---------------------------------------------#
    # 14) Color Fondo Pantalla
    # fill ()--> rellena en formato rgb nuestra interfaz
    pantalla.blit(fondo, (0, 0))

    # ---------------------------------------------#
    # 15) hacemos un  loop for por cada evento que haga el usuario
    for click in pygame.event.get():

        # 16) Boton close
        # Creamos un un boton funcional en el cual va hacer la [X] que va ha cerrar el programa cada vez que damos click , esto es una representacion de un evento
        # pygame.QUIT --> significa cuando el usuario le da click a la pantalla
        # sys.exit --> Sale del sistema cada vez que pase esa condicion
        if click.type == pygame.QUIT:
            sys.exit()
        # ---------------------------------------------#
        # 17)funciones de las teclas
        # en este apartado crearemos condiciones cuando ocurra un evento por parte del usuario
        # Si el click del loop for es == a oprimir una tecla :
        # type --> para saber que typo es
        if click.type == pygame.KEYDOWN:
            # ---------------------------------------------#
            # si el click del loop for es == a oprimir una tecla izquierda
            # key--> para saber que tipo de tecla es:
            if click.key == pygame.K_LEFT:
                # vamos a mover la figura hacia la izquirda con un ("-")
                posicion_en_MovimientoP = posicion_en_MovimientoP-0.8
            # --------------------------------------------------------------#
            # si el click del loop for es == a oprimir una tecla derecha
            # key--> para saber que tipo de tecla es:
            if click.key == pygame.K_RIGHT:
                # vamos a mover la figura hacia la derecha con un ("+")
                posicion_en_MovimientoP = posicion_en_MovimientoP+0.8
            if click.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                # agregando sonido cada vez que se dispara bala es decir cada vez que damos space
                sonido_bala.play()
                if not balaVisible:
                    posicionbalaX = posicionX
                    bala(posicionbalaY, posicionbalaY)
            # --------------------------------------------------------------#
        # 18)Tecla Derecha y Tecla Izquierda  cuando se dejan de presionar
        # si el click del loop for es == a dejar de presionar la tecla:
        if click.type == pygame.KEYUP:
            # si el click del loop for es == a la tecla izquierda o tecla derecha :
            if click.key == pygame.K_LEFT or click.key == pygame.K_RIGHT:
                posicion_en_MovimientoP = 0

    # --------------------------------------------#
    # 19 )Jugador Enemigo
    # En esta parte modificamos la variable PosicionXE para sumarle la variable donde esta nuestro jugador en movimiento
    for e in range(cantidad_enemigos):
        posicionXE[e] += posicion_en_MovimientoX_E[e]
        # ----------------------------------------------------------#
        # 20) Mantener el Enemigo  dentro de los bordes de la interfaz
        # Si el jugador en el eje X es menor o igual  a 0 en el eje x
        if posicionXE[e] <= 0:
            # La posicion va hacer 0.3 es decir se va ir para la derecha
            posicion_en_MovimientoX_E[e] = 0.3
            # La posicion en el eje Y va ir bajando 50 px cada vez que se cumpla la condicion
            posicionYE[e] += posicion_en_MovimientoY_E[e]
        # Si el jugador en el eje X es mayor o igual  a 736 en el eje y
        elif posicionXE[e] >= 736:
            # la posicion va a hacer -0.3 es decir se va a mover hacia la izquierda
            posicion_en_MovimientoX_E[e] = -0.3
            # La posicion en el eje Y va ir bajando 50 px cada vez que se cumpla la condicion
            posicionYE[e] += posicion_en_MovimientoY_E[e]

            # llamamos a la funcion detectar colicion
        colicion = detectarColicion(
            posicionXE[e], posicionYE[e], posicionbalaX, posicionbalaY)
        # si se cumple esta condicion
        if colicion is True:
            # Agrgando sonido cada vez que matamos al enemigo
            sonido_colicion = mixer.Sound('golpe.mp3')
            sonido_colicion.play()
            # la posicion de la bala vuelve a estar en la posicion de la nave o jugador
            posicionbalaY = 500
            # desaparece la bala
            balaVisible = False
            # va aumenta un puntaje
            puntaje = puntaje+1

            # y autamaticamente se reinicia la posicin del jugador
            posicionXE[e] = random.randint(0, 736)
            posicionYE[e] = random.randint(50, 200)
            # Llmamos a la funcion Enemigo
        enemigo(posicionXE[e], posicionYE[e], e)

    # ----------------------------------------------------------------------------------------------------------------------------------#
    # 21) jugador Principal
    # En esta parte modificamos la variable PosicionX sumarle la variable donde esta nuestro jugador en movimiento
    posicionX = posicionX+posicion_en_MovimientoP
    # --------------------------------------------#
    # 22) Mantener el jugador Principal dentro de los bordes de la interfaz
    # Si el jugador en el eje X es menor a 0 en el eje x
    if posicionX < 0:
        # La posicion va hacer 0
        posicionX = 0
    # Si el jugador en el eje X es mayor a 736 en el eje y
    elif posicionX > 736:
        # la posicion va hacer la misma
        posicionX = 736
    # --------------------------------------------#
    # 23)Movimiento bala
    if posicionbalaY <= -64:
        posicionbalaY = 500
        balaVisible = False
    if balaVisible:
        bala(posicionbalaX, posicionbalaY)
        posicionbalaY -= posicionMovimientoBalaY

    # 24)Funciones

    # Llmamos a la funcion jugador Principal
    jugador(posicionX, posicionY)
    mostrar_puntaje(textoX, texto_y)
    # update () --> para cargar
    pygame.display.update()
