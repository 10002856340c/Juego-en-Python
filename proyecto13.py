
import pygame
import sys
import random
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


def jugador(x, y):
    # blit()--> Para indicar que y en que posicion va estar en mi pantalla ( imgJugador, la posicion en el eje x ,posicion en el eje y)
    pantalla.blit(imgJugador, (x, y))


#---------------------------------------------------------------------------------------------------------------------------------------#
# 9)Creamos a nuestro Enemigo
imgEnemigo = pygame.image.load("enemigo.png")

# 10) Posicion inicial a nuestro Enemigo
# utilizamos la libreria random.randint() --> para que nos genere numeros aleatorios

# en este caso algenerarnos numeros aleatoria el enemigo va aparecer en una posicion diferente
# en el eje x va ir de ( 0, hasta el ancho de la altura en el eje y que en este caso es de 800)
# ¿Por que de 0 a 736? -- >por que recordemos que la figura tiene aproximadamente 60 px se le resta este valor
posicionXE = random.randint(0, 736)
# y en el eje Y va ir de 50 como mas alto y 200 como mas bajo
posicionYE = random.randint(50, 200)
# 11) Posicion del Enemigo  cada vez que se ejecuta el lopp while
posicion_en_MovimientoX_E = 0.3
posicion_en_MovimientoY_E = 50


def enemigo(x, y):
    # blit()--> Para indicar que y en que posicion va estar en mi pantalla ( imgJugador, la posicion en el eje x ,posicion en el eje y)
    pantalla.blit(imgEnemigo, (x, y))


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
        # 17)Tecla Derecha y Tecla Izquierda  cuando se presionan
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
    posicionXE = posicionXE+posicion_en_MovimientoX_E
    # --------------------------------------------#
    # 20) Mantener el Enemigo  dentro de los bordes de la interfaz
    # Si el jugador en el eje X es menor o igual  a 0 en el eje x
    if posicionXE <= 0:
        # La posicion va hacer 0.3 es decir se va ir para la derecha
        posicion_en_MovimientoX_E = 0.3
        # La posicion en el eje Y va ir bajando 50 px cada vez que se cumpla la condicion
        posicionYE = posicionYE + posicion_en_MovimientoY_E
    # Si el jugador en el eje X es mayor o igual  a 736 en el eje y
    elif posicionXE >= 736:
        # la posicion va a hacer -0.3 es decir se va a mover hacia la izquierda
        posicion_en_MovimientoX_E = -0.3
        # La posicion en el eje Y va ir bajando 50 px cada vez que se cumpla la condicion
        posicionYE = posicionYE + posicion_en_MovimientoY_E

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
    # 23)Funciones
    # Llmamos a la funcion jugador Principal
    jugador(posicionX, posicionY)
    # Llmamos a la funcion Enemigo
    enemigo(posicionXE, posicionYE)
    # update () --> para cargar
    pygame.display.update()
