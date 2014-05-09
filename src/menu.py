import pygame
from pygame.locals import *
from button import Button

class Menu:

	def __init__(self):
		self.playButton=Button(200,200,"../assets/images/menu/playButton.png","../assets/images/menu/playButtonHighlight.png")
		self.optionsButton=Button(200,300,"../assets/images/menu/optionsButton.png","../assets/images/menu/optionsButtonHighlight.png")
		self.highScoresButton=Button(200,400,"../assets/images/menu/highScoresButton.png","../assets/images/menu/highScoresButtonHighlight.png")
		self.selectLocation = 0
		self.cooldown = 0

	def drawMenu(self,screen):
		pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
		if self.selectLocation == 0:
			self.playButton.isHighlight=True
			self.optionsButton.isHighlight=False
			self.highScoresButton.isHighlight=False
		elif self.selectLocation == 1:
			self.playButton.isHighlight=False
			self.optionsButton.isHighlight=True
			self.highScoresButton.isHighlight=False
		elif self.selectLocation == 2:
			self.playButton.isHighlight=False
			self.optionsButton.isHighlight=False
			self.highScoresButton.isHighlight=True
		self.playButton.drawButton(screen)
		self.optionsButton.drawButton(screen)
		self.highScoresButton.drawButton(screen)
		if self.cooldown <= 5:
			self.cooldown += 1

	def keyPress(self,key):
		if self.cooldown > 5:
			if key[K_w] == 1:
				self.selectLocation -= 1
			elif key[K_s] == 1:
				self.selectLocation += 1
			elif key[K_UP] == 1:
				self.selectLocation -= 1
			elif key[K_DOWN] == 1:
				self.selectLocation += 1
			if self.selectLocation > 2:
				self.selectLocation = 0
			elif self.selectLocation < 0:
				self.selectLocation = 2
			self.cooldown = 0
