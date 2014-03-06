import pygame
from world import World
from hud import Hud
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
		self.screen.set_colorkey(self.backgroundColor)
		self.hud = Hud()
		self.world = World(self.screen)
	def gameLoop(self):
		while self.exiting == False:
			self.getButtonPress()
			self.world.worldUpdate()
			self.draw()
			pygame.display.flip()
			self.Clock.tick(40)
			pygame.display.set_caption(str(self.Clock.get_fps()))
		pygame.quit()
	def draw(self):
		self.screen.fill(self.backgroundColor)
		if self.inLevel:
			self.world.drawLevel(self.screen)
			self.hud.drawHUD(self.screen,self.world.score)
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
					pygame.quit()
				else:
					self.world.character.keyPress(key)
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.world.character.mousePress(pygame.mouse.get_pressed(),self.screen)
