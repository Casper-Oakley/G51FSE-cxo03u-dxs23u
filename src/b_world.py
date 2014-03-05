import pygame,random
from player import Character
from enemy1 import Enemy1
from levelblock import Levelblock

class World:
	currentX=0
	currentY=0
	enemy1List=[]

	def __init__(self,screen):
		self.loadLevel(screen)

	def loadLevel(self, screen):
		self.backgroundImage=pygame.image.load("../assets/images/world/Pleiades_large.jpg")
		self.genLevel(160,screen)
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
		self.character.applyGravity(self.levelList[self.character.currentX/64].y)
		for i in range(len(self.enemy1List)):
			self.enemy1List[i].move()

	def genEnemy1(self,screen,x,y):
		tempEn = Enemy1(x,y,screen)
		self.enemy1List.append(tempEn)

	def genLevel(self,levelsize,screen):
		self.levelList=[]
		random.seed()
		levelBuff = 12
		for i in range(levelBuff):
			if i==0:
				blockTemp = Levelblock(i*64,480-4*12,2,0,-1)
				self.levelList.append(blockTemp)
			else:
				yval=480-48*(1+(i/12))
				blockTemp = Levelblock(i*64,yval,5,0,-1)
				self.levelList.append(blockTemp)
		for i in range(levelBuff,levelsize-levelBuff-1):
			yval=480-48*(i/12)
			blockTemp = Levelblock(10*64,yval,5,0,-1)
			self.levelList.append(blockTemp)
		for i in range(levelBuff):
			self.levelList[i].load(screen)
			if self.levelList[i].enemy1ID >= 0:
				self.genEnemy1(screen,self.levelList[i].x,self.levelList[i].y)
				self.enemy1List[self.levelList[i].enemy1ID].load(screen)


	def drawBlocksOnScreen(self,screen):
		levelBuff=12
		if self.levelList[0].x+self.levelList[0].imageTop.get_width()<0:
			self.levelList.pop(0)
			self.levelList[levelBuff-1].load(screen)
			if self.levelList[levelBuff-1].enemy1ID >= 0:
				self.genEnemy1(screen,self.levelList[levelBuff-1].x,self.levelList[levelBuff-1].y)
				self.enemy1List[self.levelList[levelBuff-1].enemy1ID].load(screen)
		for i in range(levelBuff):
			self.levelList[i].move()
			self.levelList[i].draw(screen)
			if self.levelList[i].enemy1ID >= 0:
				print self.levelList[i].enemy1ID
				self.enemy1List[self.levelList[i].enemy1ID].draw(screen)
