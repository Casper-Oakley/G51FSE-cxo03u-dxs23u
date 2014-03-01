import pygame
from world import World
from pygame.locals import *


class Window:
	width=640
	height=480
	exiting = False
	inLevel = True
	backgroundColor = 255,0,255
	Clock = pygame.time.Clock()
	def setWindow(self):
		self.screen = pygame.display.set_mode((self.width,self.height))
		self.screen.fill(self.backgroundColor)
		pygame.key.set_repeat(1,1)
		self.screen.set_colorkey((255,0,255))
		self.world = World()
		self.world.loadLevel(self.screen)
	def gameLoop(self):
		while self.exiting == False:
			self.getButtonPress()
			self.world.worldUpdate()
			self.draw()
			pygame.display.flip()
			self.Clock.tick(120)
			pygame.display.set_caption(str(self.Clock.get_fps()))
		pygame.quit()
	def draw(self):
		self.screen.fill(self.backgroundColor)
		if self.inLevel:
			self.world.drawLevel(self.screen)
		else:
			pygame.quit()

	def getButtonPress(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.exit()
			if event.type == KEYDOWN:
				key = pygame.key.get_pressed()
				if key[K_ESCAPE] == 1:
					print "exiting..."
					exiting = True
				else:
					self.world.character.keyPress(key)
