import pygame
from pygame.locals import *
from random import *
import math
def main():
	pygame.init()
	pygame.font.init()
	Clock = pygame.time.Clock()
	exiting = False
	size = width, height = 400, 400
	background = 0,0,0
	screen = pygame.display.set_mode(size)
	screen.fill(background)
	pygame.key.set_repeat(1,1)
	while exiting == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.exit()
			if event.type == KEYDOWN:
				key = pygame.key.get_pressed()
				if key[K_ESCAPE] == 1:
					print "exiting..."
					exiting = True
		pygame.display.flip()
		Clock.tick(120)
		pygame.display.set_caption(str(Clock.get_fps()))
	pygame.quit()
main()
