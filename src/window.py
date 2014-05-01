import pygame
from world import World
from hud import Hud
from pygame.locals import *


class Window:

	def __init__(self):
		self.width=640
		self.height=480
		self.exiting = False
		self.inLevel = True
		self.backgroundColor = 255,0,255
		self.Clock = pygame.time.Clock()
		self.hud = Hud()
#does python prerequisites to run game and creates base instances
	def setWindow(self):
		self.screen = pygame.display.set_mode((self.width,self.height))
		self.screen.fill(self.backgroundColor)
		pygame.key.set_repeat(1,1)
		self.screen.set_colorkey(self.backgroundColor)
		self.hud.loadHUD(self.screen)
		self.inGame=True
		self.loadWorld()

	def loadWorld(self):
		self.world = World(self.screen)
#main game loop, controls world and menu interaction, along with frame rate
	def gameLoop(self):
		while self.exiting == False:
			self.getButtonPress()
			if self.inGame:
				self.world.worldUpdate()
				self.draw()
				pygame.display.flip()
				self.Clock.tick(40)
				pygame.display.set_caption(str(self.Clock.get_fps()))
				self.inGame=self.world.isGame
			else:
				self.hud.restart(self.screen,self.world.score)
				pygame.display.flip()
				self.screen.fill(self.backgroundColor)
				self.Clock.tick(40)
		pygame.quit()

#draws the correct menu
	def draw(self):
		self.screen.fill(self.backgroundColor)
		if self.inLevel:
			self.world.drawLevel(self.screen)
			self.hud.drawHUD(self.screen,self.world.score,self.world.character.lives)
		else:
			pygame.quit()

#recieves input and passes it to appropriate location
	def getButtonPress(self):
		if self.inGame:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.exit()
				if event.type == KEYDOWN:
					key = pygame.key.get_pressed()
					if key[K_ESCAPE] == 1:
						pygame.quit()
					else:
						self.world.character.keyPress(key)
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.world.character.mousePress(pygame.mouse.get_pressed(),self.screen)
		else:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.exit()
				if event.type == KEYDOWN:
					key = pygame.key.get_pressed()
					if key[K_SPACE] == 1:
						self.loadWorld()
						self.inGame = True
					elif key[K_ESCAPE] == 1:
						pygame.quit()
