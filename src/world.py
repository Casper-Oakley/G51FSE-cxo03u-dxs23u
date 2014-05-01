import pygame,random
from player import Character
from enemy1 import Enemy1
from levelPlat import Levelplat

class World:

	def __init__(self,screen):
		self.currentX=0
		self.currentY=0
		self.score=0
		self.enemy1List=[]
		self.speed=8
		self.isGame=True
		self.loadLevel(screen)

#on load method to generate a level inc all assets
	def loadLevel(self, screen):
		self.backgroundImage=pygame.image.load("../assets/images/world/iceBackground.png").convert()
		self.baseBackgroundImage=pygame.image.load(
		"../assets/images/world/iceBackgroundBase.png").convert()
		self.genLevel(500,screen)
		self.character = Character()
		self.drawLevel(screen)

#function to draw level inc contents
	def drawLevel(self, screen):
		screen.blit(self.baseBackgroundImage,(0,0))
		screen.blit(self.backgroundImage,(self.currentX, self.currentY))
		

		#draw enemies
		for i in range(len(self.enemy1List)):
			self.enemy1List[i].draw(screen)

		#draw char
		self.character.draw(screen)

		#draw level blocks
		self.drawBlocksOnScreen(screen)

#main world loop to compute all actions done in frame
	def worldUpdate(self):
		self.currentX-=3
		if self.currentX < -4000:#is completely off screen
			self.currentX = 640
		self.bulletCollide()
		self.playerCollide()
		self.playerFall()
		if self.levelList[0].x +self.levelList[0].size*64> 80 + self.character.charImage.get_width()/2:
			self.character.applyGravity(self.levelList[0].y)
		else:
			self.character.applyGravity(self.levelList[1].y)
		for i in range(len(self.enemy1List)):
			self.enemy1List[i].move()
		self.score+=1
		self.speed+=0.01

#generate an enemy and store it in the enemy list
	def genEnemy1(self,screen,x,y):
		tempEn = Enemy1(x,y,screen)
		self.enemy1List.append(tempEn)

##generate the initial level blocks locations and store them
	def genLevel(self,levelsize,screen):
		self.levelList=[]
		random.seed()
		blockTemp = Levelplat(screen,1,200,12,0)
		self.levelList.append(blockTemp)
		blockTemp = Levelplat(screen,0,530,2,0)
		self.levelList.append(blockTemp)
		self.levelList[0].loadPlatform(screen)
		i=2
#loop to find appropriate heights for each level block
		while i<levelsize:
			yRan = self.levelList[i-2].y+random.randint(-100,100)
			if yRan < 200:
				yRan += 100
			elif yRan > 430:
				yRan -= 100
			blockTemp = Levelplat(screen,0,yRan,random.randint(8,12),random.randint(0,4))
			self.levelList.append(blockTemp)
			blockTemp = Levelplat(screen,0,530,random.randint(2+min(self.score/1000,2),4+min(self.score/500,3)),0)
			self.levelList.append(blockTemp)
			i+=2
		xRange=0
#load the first set of blocks inc assets
		for i in range(5):
			self.levelList[i].x = xRange
			self.levelList[i].loadPlatform(screen)
			xRange+=self.levelList[i].size*64

#draw the level blocks, including removing old ones and loading new ones
	def drawBlocksOnScreen(self,screen):
		if self.levelList[0].x+self.levelList[0].size*64<0:
			self.levelList[0].enemyList=[]
			self.levelList.pop(0)
			self.levelList[4].loadPlatform(screen)
			xRange = 0
			for i in range(4):
				xRange+=self.levelList[i].size*64
			self.levelList[4].x=xRange
		for i in range(5):
			self.levelList[i].drawBlocks(screen)
			self.levelList[i].moveBlocks(self.speed)

#for each bullet, tests if it has hit any of the enemies. If it has, kill them and add score.
	def bulletCollide(self):
		for i in self.character.bulletList:
			for j in range(5):
				for k in self.levelList[j].enemyList:
					if i.bulletRectangle.colliderect(k.enemyRectangle):
						if len(self.character.bulletList)>0:
							self.character.bulletList.remove(i)
						k.isDead = True
						k.kill()
						self.score+=50

#test if the player has collided with an enemy
	def playerCollide(self):
		for i in range(5):
			for j in self.levelList[i].enemyList:
				if j.enemyRectangle.colliderect(self.character.charRectangle):
					j.isDead = True
					j.kill()
					self.playerDeath()
	
#Test if player is dead
	def playerFall(self):
#find next block after player block
		for i in range(5):
			if self.levelList[i].x > self.character.currentX:
#if current block is water and next block 
				if self.character.currentY+self.character.charImage.get_height() > 480 or (self.character.currentY+self.character.charImage.get_height()-60>self.levelList[i].y):
					self.playerDeath()
				break
#Remove a life and end game if out of lives
	def playerDeath(self):
		if not self.character.isInvuln and self.character.lives>0:
			self.speed=8
			self.character.isInvuln=True
			self.character.currentY = 20
			self.character.lives-=1
		elif not self.character.isInvuln:
			self.isGame=False
