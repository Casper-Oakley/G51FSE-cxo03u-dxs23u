import pygame,random
from player import Character
from enemy1 import Enemy1
from levelPlat import Levelplat

class World:
	currentX=0
	currentY=0
	score=0
	enemy1List=[]
	speed=8

	def __init__(self,screen):
		self.loadLevel(screen)

	def loadLevel(self, screen):
		self.backgroundImage=pygame.image.load("../assets/images/world/IceBackground.png")
		self.genLevel(500,screen)
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
		self.bulletCollide()
		self.playerCollide()
		self.playerFall()
		self.score+=1
		self.speed+=0.01

	def genEnemy1(self,screen,x,y):
		tempEn = Enemy1(x,y,screen)
		self.enemy1List.append(tempEn)

	def genLevel(self,levelsize,screen):
		self.levelList=[]
		random.seed()
		blockTemp = Levelplat(screen,1,200,12,0)
		self.levelList.append(blockTemp)
		blockTemp = Levelplat(screen,0,530,2,0)
		self.levelList.append(blockTemp)
		self.levelList[0].loadPlatform(screen)
		i=2
		while i<levelsize:
			yRan = self.levelList[i-2].y+random.randint(-100,100)
			if yRan < 200:
				yRan += 100
			elif yRan > 480:
				yRan -= 100
			blockTemp = Levelplat(screen,0,yRan,random.randint(8,12),random.randint(0,4))
			self.levelList.append(blockTemp)
			blockTemp = Levelplat(screen,0,530,random.randint(2+min(self.score/1000,2),4+min(self.score/1000,3)),0)
			self.levelList.append(blockTemp)
			i+=2
		xRange=0
		for i in range(5):
			self.levelList[i].x = xRange
			self.levelList[i].loadPlatform(screen)
			xRange+=self.levelList[i].size*64

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

	def bulletCollide(self):
		for i in self.character.bulletList:
			for j in range(5):
				for k in self.levelList[j].enemyList:
					if i.rect1.colliderect(k.rect1):
						if len(self.character.bulletList)>0:
							self.character.bulletList.remove(i)
						k.isDead = True
						k.kill()
						self.score+=50

	def playerCollide(self):
		for i in range(5):
			for j in self.levelList[i].enemyList:
				if j.rect1.colliderect(self.character.rect1):
					self.playerDeath()
	
	def playerFall(self):
		for i in range(5):
			if self.levelList[i].x > self.character.currentX+self.character.charImage.get_width():
				if self.levelList[i-1].y>480 and self.character.currentY > self.levelList[i].y:
					playerDeath()
				break
	def playerDeath(self):
		print "DEAD"
