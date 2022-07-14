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
# 7)Posicion de nuestro jugador
posicionX = 360
posicionY = 535


def jugador():
    # blit()--> Para indicar que y en que posicion va estar en mi pantalla ( imgJugador, la posicion en el eje x ,posicion en el eje y)
    pantalla.blit(imgJugador, (posicionX, posicionY))


#---------------------------------------------------------------------------------------------------------------------------------------#
# 8) creamos un bucle while para que se ejecute nuetro programa cada ves que sea True
while True:
    # 9) Color Fondo Pantalla
    # fill ()--> rellena en formato rgb nuestra interfaz
    pantalla.fill((48, 42, 161))
    # ---------------------------------------------#
    # 10) Boton close
    # Creamos un un boton funcional en el cual va hacer la [X] que va ha cerrar el programa cada vez que damos click
    # pygame.QUIT --> significa cuando el usuario le da click a la pantalla
    # sys.exit --> Sale del sistema cada vez que pase esa condicion
    for click in pygame.event.get():
        if click.type == pygame.QUIT:
            sys.exit()
    # --------------------------------------------#
    # 11) Llamamos a la funcion previamente
    jugador()
    # update () --> para cargar
    pygame.display.update()
