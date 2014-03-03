import pygame

BLOCK_NORMAL = 0


class Levelblock:
	x=0
	y=0
	speed=1
	isGen = False
	btype=BLOCK_NORMAL

	def __init__(self,x,y,speed,btype):
		self.x=x
		self.y=y
		self.speed=speed

	def load(self,screen):
		self.imageTop=pygame.image.load("../assets/images/world/block_normal_top.png").convert()
		self.imageGround=pygame.image.load("../assets/images/world/block_normal_ground.png").convert()
		self.isGen = True

	def draw(self,screen):
		screen.blit(self.imageTop,(self.x,self.y))
		i = self.y
		while i <= 480:
			i+=self.imageGround.get_height()
			screen.blit(self.imageGround,(self.x,i))

	def move(self):
		self.x-=self.speed
