import pygame,random
from levelblock import Levelblock
from enemy1 import Enemy1

class Levelplat:

	def __init__(self,screen,x,y,size,nEnemy1):
		self.x=0
		self.y=0
		self.size=size
		self.nEnemy1=0
		self.x=x
		self.y=y
		self.nEnemy1=nEnemy1
		self.platList=[0]*12
		self.enemyList=[]

	def loadPlatform(self,screen):
		for i in range(self.size):
			## Generate a single block 
			blockTemp = Levelblock(self.x+i*64,self.y,2,0,-1)
			## Decide whether to generate enemy on this block.
			if self.nEnemy1 > 0 and random.randint(1,self.size) > 8:
				self.nEnemy1-=1
				## Generate the enemy
				tempEnemy=Enemy1(self.x+i*64,self.y-96,screen)
				## Saves the position the enemy should be drawn in ... somehow
				blockTemp.enemy1ID=len(self.enemyList)
				tempEnemy.load(screen)
				self.enemyList.append(tempEnemy)
			## Put the block into the platform
			self.platList[i]=blockTemp
		## Load all the blocks in the platform.
		for i in range(self.size):
			self.platList[i].load(screen)

	def drawBlocks(self,screen):
		counter = 0
		## for each block in the platform
		for i in range(self.size):
			## if there is any enemy here. 
			if self.platList[i].enemy1ID >= 0:
				## Draw the enemy on the block
				self.enemyList[self.platList[i].enemy1ID].draw(screen,i*64+self.x,self.y-96)
			## Draw the block
			self.platList[i].draw(screen,counter*64+self.x,self.y)
			counter+=1

	def moveBlocks(self,speed):
		self.x-=speed
