import pygame
from window import Window

def main():
	pygame.init()
	pygame.font.init()
	mainWindow = Window()
	mainWindow.setWindow()
	mainWindow.gameLoop()

if __name__ == '__main__': main()
