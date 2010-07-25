#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos

import sys, pygame
from pygame.locals import *

# Constantes


# Clases
# ---------------------------------------------------------------------

class Input:
	def __init__(self):
		self.keys = ()
	def update(self):
		self.keys = pygame.key.get_pressed()
	def isPressed(self, k):
		return self.keys[k]
	def getKeyList(self):
		return self.keys

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------



# ---------------------------------------------------------------------

def main():
	pass

if __name__ == '__main__':
	main()
