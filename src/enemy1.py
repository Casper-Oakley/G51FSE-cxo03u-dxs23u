import pygame
import math

class Enemy1:
	x=0
	y=0

	def __init__(self,x,y,screen):
		#note angle is in deg
		self.x=x
		self.y=y

	def load(self,screen):
		self.image=pygame.image.load("../assets/images/enemy/enemy1.png").convert()

	def move(self):
		self.x+=1
		self.y+=1

	def draw(self,screen):
		screen.blit(self.image,(self.x,self.y))
