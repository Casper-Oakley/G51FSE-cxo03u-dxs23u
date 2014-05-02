import pygame
import math

class Enemy2:

	def __init__(self,x,y,screen):
		#note angle is in deg
		self.x=x
		self.y=y
		self.isDead = False

	def load(self,screen):
		#self.sprite = pygame.sprite.Sprite()
		## Standard image loading and collision box setup
		self.imageAir=pygame.image.load("../assets/images/enemy/pogo1.png").convert_alpha()
		self.imageGro = pygame.image.load("../assets/images/enemy/pogo2.png").convert_alpha()
		self.rect1 = pygame.Rect(self.x,self.y,self.imageAir.get_width(),self.imageAir.get_height())
		#self.sprite.maskIm=pygame.mask.from_surface(self.image)

	
	def draw(self,screen,x,y):
		if not self.isDead:
			screen.blit(self.imageAir,(x,y))
			self.rect1.x=x
			self.rect1.y=y
	
	def kill(self):
		self.rect1.x = -50
		self.rect1.y = -50
