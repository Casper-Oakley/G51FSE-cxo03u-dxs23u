import pygame
import math

class Enemy1:

	def __init__(self,x,y,screen):
		#note angle is in deg
		self.x=x
		self.y=y
		self.isDead = False

	def load(self,screen):
		self.sprite = pygame.sprite.Sprite()
		self.image=pygame.image.load("../assets/images/enemy/snowman.png").convert_alpha()
		self.rect1 = pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
		#self.sprite.maskIm=pygame.mask.from_surface(self.image)

	def draw(self,screen,x,y):
		if not self.isDead:
			screen.blit(self.image,(x,y))
			self.rect1.x=x
			self.rect1.y=y
	
	def kill(self):
		self.rect1.x = -50
		self.rect1.y = -50
