import pygame
from pygame.locals import *
from button import Button

class Menu:

	def __init__(self):
		##on load, initiate all images and create new buttons
		self.background=pygame.image.load("../assets/images/menu/menuBackground.png")
		self.title=pygame.image.load("../assets/images/menu/menuTitle.png")
		self.playButton=Button(256,200,"../assets/images/menu/playButton.png","../assets/images/menu/playButtonHighlight.png")
		self.optionsButton=Button(256,260,"../assets/images/menu/optionsButton.png","../assets/images/menu/optionsButtonHighlight.png")
		self.highScoresButton=Button(256,320,"../assets/images/menu/highScoresButton.png","../assets/images/menu/highScoresButtonHighlight.png")
		self.quitButton=Button(256,380,"../assets/images/menu/quitButton.png","../assets/images/menu/quitButtonHighlight.png")
		self.selectLocation = 0

	def drawMenu(self,screen):
		pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
		screen.blit(self.background,(0,0))
		screen.blit(self.title,(40,20))
		##logic for selecting option by keyboard
		if self.selectLocation == 0:
			self.playButton.isHighlight=True
			self.optionsButton.isHighlight=False
			self.highScoresButton.isHighlight=False
			self.quitButton.isHighlight=False
		elif self.selectLocation == 1:
			self.playButton.isHighlight=False
			self.optionsButton.isHighlight=True
			self.highScoresButton.isHighlight=False
			self.quitButton.isHighlight=False
		elif self.selectLocation == 2:
			self.playButton.isHighlight=False
			self.optionsButton.isHighlight=False
			self.highScoresButton.isHighlight=True
			self.quitButton.isHighlight=False
		elif self.selectLocation == 3:
			self.playButton.isHighlight=False
			self.optionsButton.isHighlight=False
			self.highScoresButton.isHighlight=False
			self.quitButton.isHighlight=True
		self.playButton.drawButton(screen)
		self.optionsButton.drawButton(screen)
		self.highScoresButton.drawButton(screen)
		self.quitButton.drawButton(screen)

##function for keyboard selection logic
	def keyPress(self,key):
			if key[K_w] == 1:
				self.selectLocation -= 1
			elif key[K_s] == 1:
				self.selectLocation += 1
			elif key[K_UP] == 1:
				self.selectLocation -= 1
			elif key[K_DOWN] == 1:
				self.selectLocation += 1
			if self.selectLocation > 3:
				self.selectLocation = 0
			elif self.selectLocation < 0:
				self.selectLocation = 3
