import pygame
from pygame.locals import *
from button import Button

class Options:

	def __init__(self,currentVolume):
		self.background=pygame.image.load("../assets/images/menu/menuBackground.png")
		self.volumeUpButton=Button(256,240,"../assets/images/menu/volumeUpButton.png","../assets/images/menu/volumeUpButtonHighlight.png")
		self.volumeDownButton=Button(256,300,"../assets/images/menu/volumeDownButton.png","../assets/images/menu/volumeDownButtonHighlight.png")
		self.backButton=Button(256,400,"../assets/images/menu/backButton.png","../assets/images/menu/backButtonHighlight.png")
		self.selectLocation = 0
		self.currentVolume = currentVolume

	def drawMenu(self,screen,currentVolume):
		pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
		screen.blit(self.background,(0,0))
		##logic for selecting option by keyboard
		if self.selectLocation == 0:
			self.volumeUpButton.isHighlight=True
			self.volumeDownButton.isHighlight=False
			self.backButton.isHighlight=False
		elif self.selectLocation == 1:
			self.volumeUpButton.isHighlight=False
			self.volumeDownButton.isHighlight=True
			self.backButton.isHighlight=False
		elif self.selectLocation == 2:
			self.volumeUpButton.isHighlight=False
			self.volumeDownButton.isHighlight=False
			self.backButton.isHighlight=True
		self.volumeUpButton.drawButton(screen)
		self.volumeDownButton.drawButton(screen)
		self.backButton.drawButton(screen)
		self.drawScore(screen,currentVolume)

	def drawScore(self,screen,currentVolume):
		volumeText=pygame.font.SysFont("verdana",20,True,False)
#print volume * 100
		screen.blit(volumeText.render("Current Volume: "+str(int(currentVolume*100)),1,(255,0,0)) ,(230,150))

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
