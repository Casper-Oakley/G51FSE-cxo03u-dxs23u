import pygame
from pygame.locals import *

class Button:
	
	def __init__(self,x,y,imageLocation,imageHighlightLocation):
		##initiate images, given image locations
		self.image=pygame.image.load(imageLocation).convert_alpha()
		self.highlightImage=pygame.image.load(imageHighlightLocation).convert_alpha()
		self.buttonHitBox=pygame.Rect(x,y,self.image.get_width(),self.image.get_height())
		self.x=x
		self.y=y
		self.isHighlight=False

##function to draw image, taking into account if it's highlighted
	def drawButton(self,screen):
		mousePos=pygame.mouse.get_pos()
		if mousePos[0]>self.x and mousePos[0] < self.x+self.buttonHitBox.width and mousePos[1]>self.y and mousePos[1] < self.y+self.buttonHitBox.height:
			self.isHighlight=True
		if self.isHighlight:
			screen.blit(self.highlightImage,(self.x,self.y))
		else:
			screen.blit(self.image,(self.x,self.y))

##function to test if mouse hit button or not
	def mousePress(self,key):
		mousePos=pygame.mouse.get_pos()
		if mousePos[0]>self.x and mousePos[0] < self.x+self.buttonHitBox.width and mousePos[1]>self.y and mousePos[1] < self.y+self.buttonHitBox.height:
			return True
		return False
