import pygame
from window import Window

def main():
	## Start Pygame.
	pygame.init()
	pygame.font.init()
	## Make and initialise a window
	mainWindow = Window()
	mainWindow.setWindow()
	## Start the game.
	mainWindow.gameLoop()

if __name__ == '__main__': main()
