import pygame
from menu import Menu
from options import Options
from highscores import Highscores
from gameover import Gameover
from pause import Pause
from world import World
from hud import Hud
from pygame.locals import *

class Window:
	def __init__(self):
		self.width=640
		self.height=480
		self.exiting = False
		self.inGame = False
		self.inMenu = True
		self.inOptions = False
		self.inHighscores = False
		self.inGameover = False
		self.inPause = False
		self.counter = 0
		self.currentVolume = 1.0
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
		self.loadMenu()
##helper functions to load various menus or the game, changing logic accordingly
	def loadMenu(self):
		self.inGame = False
		self.inMenu = True
		self.inOptions = False
		self.inHighscores = False
		self.inGameover = False
		self.inPause=False
		self.menu = Menu()
	def loadOptions(self):
		self.inGame = False
		self.inMenu = False
		self.inOptions = True
		self.inHighscores = False
		self.inGameover = False
		self.inPause=False
		self.optionsMenu = Options(self.currentVolume)
	def loadHighscores(self):
		self.inGame = False
		self.inMenu = False
		self.inOptions = False
		self.inHighscores = True
		self.inGameover = False
		self.inPause=False
		self.highscoresMenu = Highscores()
	def loadWorld(self):
		self.inGame = True
		self.inMenu = False
		self.inOptions = False
		self.inHighscores = False
		self.inGameover = False
		self.inPause=False
		self.world = World(self.screen,self.currentVolume)
	def loadGameover(self):
		self.inGame = False
		self.inMenu = False
		self.inOptions = False
		self.inHighscores = False
		self.inGameover = True
		self.inPause=False
		self.gameoverMenu = Gameover()
	def loadPause(self):
		self.inGame = False
		self.inMenu = False
		self.inOptions = False
		self.inHighscores = False
		self.inGameover = False
		self.inPause = True
		self.pauseMenu = Pause()
#main game loop, controls world and menu interaction, along with frame rate
	def gameLoop(self):
		pygame.display.set_caption("Joe Schmoe Vs the Snow Bros")
		while self.exiting == False:
			self.getButtonPress()
			self.counter+=1
			if self.inGame:
				self.world.worldUpdate()
				self.inGame=self.world.isGame
				#if game over
				if not self.inGame:
#rewrite sorted file with top 10 songs
					highscores = open("../highscores.txt","r")
					highscoreStore = []
					for line in highscores:
						highscoreStore.append(int(line[:-1]))
					highscoreStore.append(self.world.score)
					highscoreStore=sorted(highscoreStore,reverse=True)
					highscoreString=""
					for i in range(10):
						highscoreString+=str(highscoreStore[i])+"\n"
					highscores.close()
					highscores = open("../highscores.txt","w")
					highscores.write(highscoreString)
					highscores.close()
					self.loadGameover()
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
			self.optionsMenu.drawMenu(self.screen,self.currentVolume)
		elif self.inHighscores:
			self.highscoresMenu.drawMenu(self.screen)
		elif self.inGameover:
			self.gameoverMenu.drawMenu(self.screen,self.world.score)
		elif self.inPause:
			self.pauseMenu.drawMenu(self.screen)
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
					elif key[K_RETURN] == 1 and self.counter > 3:
						self.loadPause()
					else:
						self.world.character.keyPress(key)
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.world.character.mousePress(pygame.mouse.get_pressed(),self.screen)
		#button cooldown counter
		if self.counter>3:
			#send simple input and recieve output from menu
			if self.inMenu:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.exit()
					if event.type == KEYDOWN:
						key=pygame.key.get_pressed()
						if key[K_ESCAPE] == 1:
							pygame.quit()
#process options for highlighted input
						elif key[K_SPACE] == 1 or key[K_RETURN] == 1:
							if self.menu.playButton.isHighlight:
								self.loadWorld()
							elif self.menu.optionsButton.isHighlight:
								self.loadOptions()
							elif self.menu.highScoresButton.isHighlight:
								self.loadHighscores()
							elif self.menu.quitButton.isHighlight:
								pygame.quit()
						else:
							self.menu.keyPress(key)
					if event.type == pygame.MOUSEBUTTONDOWN:
						#process each option when clicked
						if self.menu.playButton.mousePress(pygame.mouse.get_pressed()):
							self.loadWorld()
						elif self.menu.optionsButton.mousePress(pygame.mouse.get_pressed()):
							self.loadOptions()
						elif self.menu.highScoresButton.mousePress(pygame.mouse.get_pressed()):
							self.loadHighscores()
						elif self.menu.quitButton.mousePress(pygame.mouse.get_pressed()):
							pygame.quit()
			#send simple input and recieve output from options, changing volume
			elif self.inOptions:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.exit()
					if event.type == KEYDOWN:
						key=pygame.key.get_pressed()
						if key[K_ESCAPE] == 1:
							pygame.quit()
						elif key[K_SPACE] == 1 or key[K_RETURN] == 1:
							if self.optionsMenu.volumeUpButton.isHighlight:
								if self.currentVolume<1.0:
									self.currentVolume+=0.1
							elif self.optionsMenu.volumeDownButton.isHighlight:
								if self.currentVolume>=0.1:
									self.currentVolume-=0.1
							elif self.optionsMenu.backButton.isHighlight:
								self.loadMenu()
						else:
							self.optionsMenu.keyPress(key)
					if event.type == pygame.MOUSEBUTTONDOWN:
						if self.optionsMenu.volumeUpButton.mousePress(pygame.mouse.get_pressed()):
							if self.currentVolume<1.0:
								self.currentVolume+=0.1
						elif self.optionsMenu.volumeDownButton.mousePress(pygame.mouse.get_pressed()):
							if self.currentVolume>=0.1:
								self.currentVolume-=0.1
						elif self.optionsMenu.backButton.mousePress(pygame.mouse.get_pressed()):
							self.loadMenu()
			#send simple input and recieve output from the highscores menu
			elif self.inHighscores:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.exit()
					if event.type == KEYDOWN:
						key=pygame.key.get_pressed()
						if key[K_ESCAPE] == 1:
							pygame.quit()
						elif key[K_SPACE] == 1 or key[K_RETURN] == 1:
							if self.highscoresMenu.backButton.isHighlight:
								self.loadMenu()
					if event.type == pygame.MOUSEBUTTONDOWN:
						if self.highscoresMenu.backButton.mousePress(pygame.mouse.get_pressed()):
							self.loadMenu()
			#send simple input and recieve output from the gameover screen
			elif self.inGameover:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.exit()
					if event.type == KEYDOWN:
						key = pygame.key.get_pressed()
						if key[K_ESCAPE] == 1:
							pygame.quit()
						elif key[K_SPACE] == 1 or key[K_RETURN] == 1:
							if self.gameoverMenu.playButton.isHighlight:
								self.loadWorld()
							elif self.gameoverMenu.highScoresButton.isHighlight:
								self.loadHighscores()
						else:
							self.gameoverMenu.keyPress(key)
					if event.type == pygame.MOUSEBUTTONDOWN:
						if self.gameoverMenu.playButton.mousePress(pygame.mouse.get_pressed()):
							self.loadWorld()
						elif self.gameoverMenu.highScoresButton.mousePress(pygame.mouse.get_pressed()):
							self.loadHighscores()
			#send simple input and recieve output from the pause menu
			elif self.inPause:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.exit()
					if event.type == KEYDOWN:
						key = pygame.key.get_pressed()
						if key[K_ESCAPE] == 1:
							pygame.quit()
						elif key[K_SPACE] == 1 or key[K_RETURN] == 1:
							if self.pauseMenu.restartButton.isHighlight:
								self.loadWorld()
							elif self.pauseMenu.quitButton.isHighlight:
								self.loadMenu()
							elif self.pauseMenu.unpauseButton.isHighlight:
								self.inGame = True
								self.inPause = False
						else:
							self.pauseMenu.keyPress(key)
					if event.type == pygame.MOUSEBUTTONDOWN:
						if self.pauseMenu.restartButton.mousePress(pygame.mouse.get_pressed()):
							self.loadWorld()
						elif self.pauseMenu.quitButton.mousePress(pygame.mouse.get_pressed()):
							self.loadMenu()
						elif self.pauseMenu.unpauseButton.mousePress(pygame.mouse.get_pressed()):
							self.inGame = True
							self.inPause = False
			#reset the button cooldown counter
			self.counter = 0
