import pygame
from pygame.locals import *
from button import Button

class Options:

	def __init__(self,currentVolume):
		self.volumeUpButton=Button(200,200,"../assets/images/menu/volumeUpButton.png","../assets/images/menu/volumeUpButtonHighlight.png")
		self.volumeDownButton=Button(200,300,"../assets/images/menu/volumeDownButton.png","../assets/images/menu/volumeDownButtonHighlight.png")
		self.backButton=Button(200,400,"../assets/images/menu/backButton.png","../assets/images/menu/backButtonHighlight.png")
		self.selectLocation = 0
		self.cooldown = 0
		self.currentVolume = currentVolume

	def drawMenu(self,screen,currentVolume):
		pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
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
		if self.cooldown <= 5:
			self.cooldown += 1
		self.drawScore(screen,currentVolume)

	def drawScore(self,screen,currentVolume):
		volumeText=pygame.font.SysFont("Helvetica",20,True,False)
#print volume * 100
		screen.blit(volumeText.render("Current Volume: "+str(int(currentVolume*100)),1,(255,0,0)) ,(10,10))

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
