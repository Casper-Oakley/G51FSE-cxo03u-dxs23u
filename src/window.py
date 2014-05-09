import pygame
from menu import Menu
from options import Options
from world import World
from hud import Hud
from pygame.locals import *


class Window:

	def __init__(self):
		self.width=640
		self.height=480
		self.currentVolume=0
		self.exiting = False
		self.inGame = False
		self.inMenu = True
		self.inOptions = False
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
		self.currentVolume=pygame.mixer.music.get_volume()
		self.loadMenu()

	def loadMenu(self):
		self.inGame = False
		self.inMenu = True
		self.inOptions = False
		self.menu = Menu()

	def loadOptions(self):
		self.inGame = False
		self.inMenu = False
		self.inOptions = True
		self.optionsMenu = Options()

	def loadWorld(self):
		self.inGame = True
		self.inMenu = False
		self.inOptions = False
		self.world = World(self.screen)
#main game loop, controls world and menu interaction, along with frame rate
	def gameLoop(self):
		pygame.display.set_caption("TITLE")
		while self.exiting == False:
			self.getButtonPress()
			if self.inGame:
				self.world.worldUpdate()
				self.inGame=self.world.isGame
				#if game over
				if not self.inGame:
					print self.world.score
					highscores = open("../highscores.txt","a")
					highscores.write(str(self.world.score)+"\n");
					highscores.close()
			self.draw()
			pygame.display.flip()
			self.Clock.tick(40)
			self.screen.fill(self.backgroundColor)
		pygame.quit()

#draws the correct menu
	def draw(self):
		self.screen.fill(self.backgroundColor)
		if self.inGame:
			self.world.drawLevel(self.screen)
			self.hud.drawHUD(self.screen,self.world.score,self.world.character.lives)
		elif self.inMenu:
			self.menu.drawMenu(self.screen)
		elif self.inOptions:
			self.optionsMenu.drawMenu(self.screen)
		else:
			self.hud.restart(self.screen,self.world.score)

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
		#send simple input and recieve output from menu
		elif self.inMenu:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.exit()
				if event.type == KEYDOWN:
					key=pygame.key.get_pressed()
					if key[K_ESCAPE] == 1:
						pygame.quit()
#process options for highlighted input
					elif key[K_SPACE] == 1:
						if self.menu.playButton.isHighlight:
							self.loadWorld()
						elif self.menu.optionsButton.isHighlight:
							self.loadOptions()
							print "hello2"
						elif self.menu.highScoresButton.isHighlight:
							print "hello3"
					else:
						self.menu.keyPress(key)
				if event.type == pygame.MOUSEBUTTONDOWN:
					#process each option when clicked
					if self.menu.playButton.mousePress(pygame.mouse.get_pressed()):
						self.loadWorld()
					elif self.menu.optionsButton.mousePress(pygame.mouse.get_pressed()):
						self.loadOptions()
						print "hello2"
					elif self.menu.highScoresButton.mousePress(pygame.mouse.get_pressed()):
						print "hello3"
		#send simple input and recieve output from options
		elif self.inOptions:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.exit()
				if event.type == KEYDOWN:
					key=pygame.key.get_pressed()
					if key[K_ESCAPE] == 1:
						pygame.quit()
					elif key[K_SPACE] == 1:
						if self.optionsMenu.volumeUpButton.isHighlight:
							if self.currentVolume<1.1:
								self.currentVolume+=0.1
								pygame.mixer.music.set_volume(self.currentVolume)
						elif self.optionsMenu.volumeDownButton.isHighlight:
							if self.currentVolume>-0.1:
								self.currentVolume-=0.1
								pygame.mixer.music.set_volume(self.currentVolume)
						elif self.optionsMenu.backButton.isHighlight:
							self.loadMenu()
							print "hello3"
					else:
						self.optionsMenu.keyPress(key)
				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.optionsMenu.volumeUpButton.mousePress(pygame.mouse.get_pressed()):
						if self.currentVolume<1.0:
							self.currentVolume+=0.1
							pygame.mixer.music.set_volume(self.currentVolume)
					elif self.optionsMenu.volumeDownButton.mousePress(pygame.mouse.get_pressed()):
						if self.currentVolume>0.0:
							self.currentVolume-=0.1
							pygame.mixer.music.set_volume(self.currentVolume)
					elif self.optionsMenu.backButton.mousePress(pygame.mouse.get_pressed()):
						self.loadMenu()
						print "hello3"
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
