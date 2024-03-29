import pygame

BLOCK_NORMAL = 0

class Levelblock:
	x=0
	y=0
	speed=1
	isGen = False
	enemy1ID=-1
	btype=BLOCK_NORMAL

	def __init__(self,x,y,speed,btype,enemy1ID):
		self.x=x
		self.y=y
		self.enemy1ID=enemy1ID
		self.speed=speed

	def load(self,screen):
		## Standard image loading code.
		self.imageTop=pygame.image.load("../assets/images/world/iceTop-scale.png").convert()
		self.imageGround=pygame.image.load("../assets/images/world/iceBottom-scale.png").convert()
		self.isGen = True

	def draw(self,screen,x,y):
		## Draw the top part of the block
		screen.blit(self.imageTop,(x,y))
		## Draw repeats of the bottom part below until the bottom of the window
		i = y
		while i <= 480:
			i+=self.imageGround.get_height()
			screen.blit(self.imageGround,(x,i))

	def move(self):
		self.x-=self.speed
