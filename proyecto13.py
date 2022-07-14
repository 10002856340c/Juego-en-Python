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
# 6)Creamos un un boton funcional en el cual va hacer la [X] que va ha cerrar el programa cada vez que damos click ,
# pygame.QUIT --> significa cuando el usuario le da click a la pantalla
# sys.exit --> Sale del sistema cada vez que pase esa condicion
while True:
    for click in pygame.event.get():
        if click.type == pygame.QUIT:
            sys.exit()
    
