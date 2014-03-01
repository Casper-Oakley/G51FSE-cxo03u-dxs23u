import pygame
from window import Window
from pygame.locals import *
from random import *
import math

def main():
	pygame.init()
	pygame.font.init()
	mainWindow = Window()
	mainWindow.setWindow()
	mainWindow.gameLoop()

main()
