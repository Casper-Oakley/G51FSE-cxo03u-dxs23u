import pygame
import math

class Bullet(pygame.sprite.Sprite):
	x=0
	y=0
	speed=30

#constructor to setup initial vars
	def __init__(self,x,y,angle,screen):
		#note angle is in deg
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.angle=angle
		self.load(screen)

#load the image and generate a rectangle for the bullet for hit box
	def load(self,screen):
		## Standard image loading and collision box setup
		self.image=pygame.image.load("../assets/images/other/bulletBasic.png").convert_alpha()
		self.bulletRectangle = pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
		self.draw(screen)

#move the bullet and rectangle
	def move(self):
		## Move self coordinates
		self.x+=self.speed*math.cos(math.radians(self.angle))
		self.y+=self.speed*math.sin(math.radians(self.angle))
		## update collision rectangle
		self.bulletRectangle.x=self.x
		self.bulletRectangle.y=self.y

#draw the bullet on screen
	def draw(self,screen):
		screen.blit(self.image,(self.x,self.y))
