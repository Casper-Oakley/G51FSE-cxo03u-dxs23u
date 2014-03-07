import pygame,random
from levelblock import Levelblock
from enemy1 import Enemy1

class Levelplat:

	def __init__(self,screen,x,y,size,nEnemy1,speed):
		self.speed=speed
		self.x=0
		self.y=0
		self.size=0
		self.nEnemy1=0
		self.x=x
		self.y=y
		self.size=size
		self.nEnemy1=nEnemy1
		self.platList=[0]*12
		self.enemyList=[]

	def loadPlatform(self,screen):
		for i in range(self.size):
			blockTemp = Levelblock(self.x+i*64,self.y,2,0,-1)
			if self.nEnemy1 > 0 and random.randint(1,self.size) > 8:
				self.nEnemy1-=1
				tempEnemy=Enemy1(self.x+i*64,self.y-96,screen)
				blockTemp.enemy1ID=len(self.enemyList)
				tempEnemy.load(screen)
				self.enemyList.append(tempEnemy)
			self.platList[i]=blockTemp
		for i in range(self.size):
			self.platList[i].load(screen)

	def drawBlocks(self,screen):
		counter = 0
		for i in range(self.size):
			if self.platList[i].enemy1ID >= 0:
				self.enemyList[self.platList[i].enemy1ID].draw(screen,i*64+self.x,self.y-96)
			self.platList[i].draw(screen,counter*64+self.x,self.y)
			counter+=1

	def moveBlocks(self):
		self.x-=self.speed
