import pygame,random
from player import Character
from enemy1 import Enemy1
from levelPlat import Levelplat

class World:
	currentX=0
	currentY=0
	enemy1List=[]

	def __init__(self,screen):
		self.loadLevel(screen)

	def loadLevel(self, screen):
		self.backgroundImage=pygame.image.load("../assets/images/world/IceBackground.png")
		self.genLevel(50,screen)
		self.character = Character()
		self.drawLevel(screen)

	def drawLevel(self, screen):
		#self.genEnemy1(screen)
		#draw background
		screen.blit(self.backgroundImage,(self.currentX, self.currentY))

		#draw enemies
		for i in range(len(self.enemy1List)):
			self.enemy1List[i].draw(screen)

		#draw char
		self.character.draw(screen)

		#draw level blocks
		self.drawBlocksOnScreen(screen)

	def worldUpdate(self):
		self.currentX-=1
		if self.levelList[0].x +self.levelList[0].size*64> 80 + self.character.charImage.get_width()/2:
			self.character.applyGravity(self.levelList[0].y)
		else:
			self.character.applyGravity(self.levelList[1].y)
		for i in range(len(self.enemy1List)):
			self.enemy1List[i].move()

	def genEnemy1(self,screen,x,y):
		tempEn = Enemy1(x,y,screen)
		self.enemy1List.append(tempEn)

	def genLevel(self,levelsize,screen):
		self.levelList=[]
		random.seed()
		blockTemp = Levelplat(screen,1,200,12,0)
		self.levelList.append(blockTemp)
		self.levelList[0].loadPlatform(screen)
		for i in range(1,levelsize):
			yRan = self.levelList[i-1].y+random.randint(-100,100)
			if yRan < 200:
				yRan += 100
			elif yRan > 480:
				yRan -= 100
			blockTemp = Levelplat(screen,0,yRan,random.randint(8,12),0)
			self.levelList.append(blockTemp)
		xRange=0
		for i in range(5):
			self.levelList[i].x = xRange
			self.levelList[i].loadPlatform(screen)
			xRange+=self.levelList[i].size*64

	def drawBlocksOnScreen(self,screen):
		if self.levelList[0].x+self.levelList[0].size*64<0:
			self.levelList.pop(0)
			self.levelList[4].loadPlatform(screen)
			xRange = 0
			for i in range(4):
				xRange+=self.levelList[i].size*64
			self.levelList[4].x=xRange
		for i in range(5):
			self.levelList[i].drawBlocks(screen)
			self.levelList[i].moveBlocks()
