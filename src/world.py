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
		self.backgroundImage=pygame.image.load("../assets/images/world/Pleiades_large.jpg")
		self.genLevel(20,screen)
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
		#self.character.applyGravity(self.levelList[self.character.currentX/64].y)
		for i in range(len(self.enemy1List)):
			self.enemy1List[i].move()

	def genEnemy1(self,screen,x,y):
		tempEn = Enemy1(x,y,screen)
		self.enemy1List.append(tempEn)

	def genLevel(self,levelsize,screen):
		self.levelList=[]
		random.seed()
		blockTemp = Levelplat(screen,1,200,12)
		self.levelList.append(blockTemp)
		self.levelList[0].loadPlatform(screen)
		for i in range(1,levelsize):
			blockTemp = Levelplat(screen,640,random.randint(100,400),12)
			self.levelList.append(blockTemp)
			#self.levelList[i].loadPlatform(screen)
		xRange=0
		for i in range(5):
			xRange+=self.levelList[i].size*64
			self.levelList[i].x = xRange
			self.levelList[i].loadPlatform(screen)
		#for i in range(levelBuff):
			#self.levelList[i].load(screen)
			#if self.levelList[i].enemy1ID >= 0:
				#self.genEnemy1(screen,self.levelList[i].x,self.levelList[i].y)
				#self.enemy1List[self.levelList[i].enemy1ID].load(screen)


	def drawBlocksOnScreen(self,screen):
		if self.levelList[0].x+self.levelList[0].size*64<0:
			self.levelList.pop(0)
			blockTemp = Levelplat(screen,0,200,12)
			self.levelList.append(blockTemp)
			self.levelList[4].loadPlatform(screen)
			xRange = 0
			for i in range(5):
				xRange+=self.levelList[i].size*64
			self.levelList[4].x=xRange
			#if self.levelList[3].enemy1ID >= 0:
				#self.genEnemy1(screen,self.levelList[levelBuff-1].x,self.levelList[levelBuff-1].y)
				#self.enemy1List[self.levelList[levelBuff-1].enemy1ID].load(screen)
		for i in range(5):
			self.levelList[i].drawBlocks(screen)
			self.levelList[i].moveBlocks()
			#if self.levelList[i].enemy1ID >= 0:
			#	print self.levelList[i].enemy1ID
			#	self.enemy1List[self.levelList[i].enemy1ID].draw(screen)
