import pygame
import math

class Bullet(pygame.sprite.Sprite):
	x=0
	y=0
	speed=30

	def __init__(self,x,y,angle,screen):
		#note angle is in deg
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.angle=angle
		self.load(screen)

	def load(self,screen):
		#self.sprite = pygame.sprite.Sprite()
		self.image=pygame.image.load("../assets/images/other/bullet.gif").convert()
		self.rect1 = pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
		#self.sprite.mask=pygame.mask.from_surface(self.image)
		self.draw(screen)

	def move(self):
		self.x+=self.speed*math.cos(math.radians(self.angle))
		self.y+=self.speed*math.sin(math.radians(self.angle))
		self.rect1.x=self.x
		self.rect1.y=self.y

	def draw(self,screen):
		screen.blit(self.image,(self.x,self.y))
