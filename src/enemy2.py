import pygame
import math

class Enemy2:

	def __init__(self,x,y,screen):
		#note angle is in deg
		self.x=x
		self.y=y
		self.isDead = False
		self.isJump = False
		self.yOffset = 0
		self.vSpeed = 0

	def load(self,screen):
		## Standard image loading and collision box setup
		self.imageAir=pygame.image.load("../assets/images/enemy/pogo1.png").convert_alpha()
		self.imageGro = pygame.image.load("../assets/images/enemy/pogo2.png").convert_alpha()
		self.enemyRectangle = pygame.Rect(self.x,self.y,self.imageAir.get_width(),self.imageAir.get_height())

	
	def draw(self,screen,x,y):
		self.jump()
		if not self.isDead:
			if self.yOffset > 10:
				screen.blit(self.imageAir,(x,y-self.yOffset))
			else:
				screen.blit(self.imageGro,(x,y-self.yOffset))
			self.enemyRectangle.x=x
			self.enemyRectangle.y=y-self.yOffset
	
	def kill(self):
		self.enemyRectangle.x = -50
		self.enemyRectangle.y = -50

	def jump(self):
		if not self.isJump:
			self.vSpeed = 24
			self.isJump = True
		elif self.yOffset<0:
			self.yOffset = 0
			self.isJump = False
		else:
			self.vSpeed -= 1.6
			self.yOffset += self.vSpeed
