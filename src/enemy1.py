import pygame
import math

class Enemy1:

#constructor to setup initial vars
	def __init__(self,x,y,screen):
		#note angle is in deg
		self.x=x
		self.y=y
		self.isDead = False

#load the image and generate a rectangle for the enemy
	def load(self,screen):
		self.image=pygame.image.load("../assets/images/enemy/snowman.png").convert_alpha()
		self.enemyRectangle = pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())

#draw the enemy, if it lives
	def draw(self,screen,x,y):
		if not self.isDead:
			screen.blit(self.image,(x,y))
			self.enemyRectangle.x=x
			self.enemyRectangle.y=y
	
#remove the enemy from the area to remove potential death problems
	def kill(self):
		self.enemyRectangle.x = -50
		self.enemyRectangle.y = -50
