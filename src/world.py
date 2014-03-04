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
		print self.levelList[self.character.currentX/64].x
		for i in range(len(self.enemy1List)):
			self.enemy1List[i].move()

	def genEnemy1(self,screen):
		random.seed()
		tempEn = Enemy1(random.randint(0,640),random.randint(0,480),screen)
		self.enemy1List.append(tempEn)

	def genLevel(self,levelsize,screen):
		self.levelList=[]
		random.seed()
		levelBuff = 12
		for i in range(levelBuff):
			if i==0:
				blockTemp = Levelblock(i*64,480-4*12,2,0)
				self.levelList.append(blockTemp)
			else:
				yval=480-48*(1+(i/12))
				blockTemp = Levelblock(i*64,yval,5,0)
				self.levelList.append(blockTemp)
		for i in range(levelBuff,levelsize-levelBuff-1):
			yval=480-48*(i/12)
			blockTemp = Levelblock(10*64,yval,5,0)
			self.levelList.append(blockTemp)
		for i in range(levelBuff):
			self.levelList[i].load(screen)


	def drawBlocksOnScreen(self,screen):
		levelBuff=12
		if self.levelList[0].x+self.levelList[0].imageTop.get_width()<0:
			self.levelList.pop(0)
			self.levelList[levelBuff-1].load(screen)
		for i in range(levelBuff):
			self.levelList[i].move()
			self.levelList[i].draw(screen)
