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
		self.imageTop=pygame.image.load("../assets/images/world/block_normal_top.png").convert()
		self.imageGround=pygame.image.load("../assets/images/world/block_normal_ground.png").convert()
		self.isGen = True

	def draw(self,screen,x,y):
		screen.blit(self.imageTop,(x,y))
		i = y
		while i <= 480:
			i+=self.imageGround.get_height()
			screen.blit(self.imageGround,(x,i))

	def move(self):
		self.x-=self.speed
