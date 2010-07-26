#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *

from constants import *
from map import Map
from actor import Actor
from camera import Camera
from images import load_image
from input import Input

# Constantes
WIDTH = 640
HEIGHT = 480

# Globales

# Clases
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

def salir(keys):
	for eventos in pygame.event.get():
		if eventos.type == QUIT:
			sys.exit(0)
		if keys[K_ESCAPE]:
			sys.exit(0)

# ---------------------------------------------------------------------

def main():
	
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Engine RPG")

	clock = pygame.time.Clock()
	#rejilla = load_image('resources/graphics/rejilla.png', True)
	
	map_loaded = Map("pruebas.tmx")
	heroe = Actor(map_loaded)
	camara = Camera(map_loaded, heroe)
	inp = Input()
	while True:
		time = clock.tick(40)
		inp.update()
		salir(inp.getKeyList())
		
		id = heroe.mover(map_loaded, inp)
		heroe.update(id)
		camara.update(screen, map_loaded, heroe)
		camara.show_fps(screen, clock.get_fps())
		#screen.blit(rejilla, (0, 0))
		
		pygame.display.flip()
	return 0

if __name__ == '__main__':
	pygame.init()
	main()
