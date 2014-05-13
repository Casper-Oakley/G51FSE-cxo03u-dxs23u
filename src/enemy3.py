import pygame,random
import math

class Enemy3:

	def __init__(self,x,y,screen):
		#note angle is in deg
		self.x=x
		self.y=y
		self.isDead = False
		self.isJump = False
		self.xOffset = 0
		self.animIndex = 0

	def load(self,screen):
		## Standard image loading and collision box setup
		##Animation cycle list, same as for player
		self.enemyRunCycleList = []
		self.enemyRunCycleList.append(pygame.image.load("../assets/images/enemy/wingedChainsaw1a.png").convert_alpha())
		self.enemyRunCycleList.append(pygame.image.load("../assets/images/enemy/wingedChainsaw1b.png").convert_alpha())
		self.enemyRunCycleList.append(pygame.image.load("../assets/images/enemy/wingedChainsaw1c.png").convert_alpha())
		self.enemyRunCycleList.append(pygame.image.load("../assets/images/enemy/wingedChainsaw1d.png").convert_alpha())
		self.enemyRunCycleList.append(pygame.image.load("../assets/images/enemy/wingedChainsaw1e.png").convert_alpha())
		self.enemyImage=self.enemyRunCycleList[0]
		self.enemyRectangle = pygame.Rect(self.x,self.y,self.enemyImage.get_width(),self.enemyImage.get_height())
		random.seed()
		self.xSpeed = random.randint(4,10)

	
	def draw(self,screen,x,y):
		if not self.isDead:
			self.xOffset -= self.xSpeed
			self.animIndex = (self.animIndex+1)%len(self.enemyRunCycleList) 
			self.enemyImage = self.enemyRunCycleList[self.animIndex]
			screen.blit(self.enemyImage,(x+self.xOffset,y-120))
			self.enemyRectangle.x=x+self.xOffset
			self.enemyRectangle.y=y-120
	
	def kill(self):
		self.enemyRectangle.x = -50
		self.enemyRectangle.y = -50
