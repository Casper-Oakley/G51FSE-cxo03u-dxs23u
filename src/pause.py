import pygame
from pygame.locals import *
from button import Button

class Pause:

	def __init__(self):
		self.restartButton=Button(256,200,"../assets/images/menu/restartButton.png","../assets/images/menu/restartButtonHighlight.png")
		self.unpauseButton=Button(256,300,"../assets/images/menu/unpauseButton.png","../assets/images/menu/unpauseButtonHighlight.png")
		self.quitButton=Button(256,400,"../assets/images/menu/quitButton.png","../assets/images/menu/quitButtonHighlight.png")
		self.selectLocation = 0

	def drawMenu(self,screen):
		pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
		if self.selectLocation == 0:
			self.restartButton.isHighlight=True
			self.unpauseButton.isHighlight=False
			self.quitButton.isHighlight=False
		elif self.selectLocation == 1:
			self.restartButton.isHighlight=False
			self.unpauseButton.isHighlight=True
			self.quitButton.isHighlight=False
		elif self.selectLocation == 2:
			self.restartButton.isHighlight=False
			self.unpauseButton.isHighlight=False
			self.quitButton.isHighlight=True
		self.restartButton.drawButton(screen)
		self.unpauseButton.drawButton(screen)
		self.quitButton.drawButton(screen)

	def keyPress(self,key):
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
