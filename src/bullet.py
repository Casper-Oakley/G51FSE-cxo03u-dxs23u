import pygame
import math

class Bullet:
	x=0
	y=0
	speed=30

	def __init__(self,x,y,angle,screen):
		#note angle is in deg
		self.x=x
		self.y=y
		self.angle=angle
		self.load(screen)

	def load(self,screen):
		self.image=pygame.image.load("../assets/images/other/bullet.gif").convert()
		self.draw(screen)

	def move(self):
		self.x+=self.speed*math.cos(math.radians(self.angle))
		self.y+=self.speed*math.sin(math.radians(self.angle))

	def draw(self,screen):
		screen.blit(self.image,(self.x,self.y))
