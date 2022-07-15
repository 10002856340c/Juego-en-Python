
import pygame
import sys

# 1) importamos la libreria pygame
# 2) inicializamos la libreria pygame con .init para traer todos los atributos y herramientas que tiene pygame
pygame.init()
#---------------------------------------------------------------------------------------------------------------------------------------#

# 3) Pantalla
# Creamos nuestra Pantalla de inicio del programa, guardandola en una variable, asignadole los pixeles (height,weight)
pantalla = pygame.display.set_mode((800, 600))
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
#---------------------------------------------------------------------------------------------------------------------------------------#
# 7)Posicion inicial de nuestro jugador
posicionX = 360
posicionY = 535
# 8) Posicion del jugador cuando se opriman las teclas
posicion_en_Movimiento = 0


def jugador(x, y):
    # blit()--> Para indicar que y en que posicion va estar en mi pantalla ( imgJugador, la posicion en el eje x ,posicion en el eje y)
    pantalla.blit(imgJugador, (x, y))


#---------------------------------------------------------------------------------------------------------------------------------------#
# 9) creamos un bucle while para que se ejecute nuetro programa cada ves que sea True
while True:
    # 10 ) Movimiento del jugador

    # ---------------------------------------------#
    # 11) Color Fondo Pantalla
    # fill ()--> rellena en formato rgb nuestra interfaz
    pantalla.fill((48, 42, 161))

    # ---------------------------------------------#
    # 12) hacemos un  loop for por cada evento que haga el usuario
    for click in pygame.event.get():

        # 13) Boton close
        # Creamos un un boton funcional en el cual va hacer la [X] que va ha cerrar el programa cada vez que damos click , esto es una representacion de un evento
        # pygame.QUIT --> significa cuando el usuario le da click a la pantalla
        # sys.exit --> Sale del sistema cada vez que pase esa condicion
        if click.type == pygame.QUIT:
            sys.exit()
        # ---------------------------------------------#
        # 14)Tecla Derecha y Tecla Izquierda  cuando se presionan
        # en este apartado crearemos condiciones cuando ocurra un evento por parte del usuario
        # Si el click del loop for es == a oprimir una tecla :
        # type --> para saber que typo es
        if click.type == pygame.KEYDOWN:
            # ---------------------------------------------#
            # si el click del loop for es == a oprimir una tecla izquierda
            # key--> para saber que tipo de tecla es:
            if click.key == pygame.K_LEFT:
                # vamos a mover la figura hacia la izquirda con un ("-")
                posicion_en_Movimiento = posicion_en_Movimiento-0.5
            # --------------------------------------------------------------#
            # si el click del loop for es == a oprimir una tecla derecha
            # key--> para saber que tipo de tecla es:
            if click.key == pygame.K_RIGHT:
                # vamos a mover la figura hacia la derecha con un ("+")
                posicion_en_Movimiento = posicion_en_Movimiento+0.5
            # --------------------------------------------------------------#
        # 15)Tecla Derecha y Tecla Izquierda  cuando se dejan de presionar
        # si el click del loop for es == a dejar de presionar la tecla:
        if click.type == pygame.KEYUP:
            # si el click del loop for es == a la tecla izquierda o tecla derecha :
            if click.key == pygame.K_LEFT or click.key == pygame.K_RIGHT:
                posicion_en_Movimiento = 0

    # --------------------------------------------#
    # 16 )En esta parte modificamos la variable PosicionX sumarle la variable donde esta nuestro jugador en movimiento
    posicionX = posicionX+posicion_en_Movimiento
    jugador(posicionX, posicionY)
    # --------------------------------------------#
    # 17) Mantener el jugador dentro de los bordes de la interfaz
    # Si el jugador en el eje X es menor a 0 en el eje x
    if posicionX < 0:
        # La posicion va hacer 0
        posicionX = 0
    # Si el jugador en el eje X es mayor a 736
    elif posicionX > 736:
        # la posicion va hacer la misma
        posicionX = 736
    # --------------------------------------------#
    # update () --> para cargar
    pygame.display.update()
