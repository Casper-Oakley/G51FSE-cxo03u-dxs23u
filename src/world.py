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
	isGame=True

	def __init__(self,screen):
		self.loadLevel(screen)

	def loadLevel(self, screen):
		## Standard image loading
		self.backgroundImage=pygame.image.load("../assets/images/world/iceBackground.png").convert()
		self.baseBackgroundImage=pygame.image.load(
		"../assets/images/world/iceBackgroundBase.png").convert()
		## Create level, character
		self.genLevel(500,screen)
		self.character = Character()
		## Draw the level once
		self.drawLevel(screen)

	def drawLevel(self, screen):
		#self.genEnemy1(screen)
		## Draw background
		screen.blit(self.baseBackgroundImage,(0,0))
		screen.blit(self.backgroundImage,(self.currentX, self.currentY))
		

		## Draw enemies
		for i in range(len(self.enemy1List)):
			self.enemy1List[i].draw(screen)

		## Draw character
		self.character.draw(screen)

		## Draw level blocks
		self.drawBlocksOnScreen(screen)

	def worldUpdate(self):
		## Moves itself backwards to simulate the 
		## character running forwars against the screen
		self.currentX-=3
		## Loop background around
		if self.currentX < -4000:#is completely off screen
			self.currentX = 640
		## Tests which set of platforms the character is on 
		## and sets the height of the floor used by the 
		## gravity function accordingly
		if (self.levelList[0].x+self.levelList[0].size * 64) > (80+self.character.charImage.get_width() / 2):
			self.character.applyGravity(self.levelList[0].y)
		else:
			self.character.applyGravity(self.levelList[1].y)
		## Move the enemies forward
		for i in range(len(self.enemy1List)):
			self.enemy1List[i].move()
		## Check for collisions
		self.bulletCollide()
		self.playerCollide()
		## Move the player, update score and increase speed
		self.playerFall()
		self.score+=1
		self.speed+=0.01

	def genEnemy1(self,screen,x,y):
		## create an enemy1 (snowman)
		tempEn = Enemy1(x,y,screen)
		self.enemy1List.append(tempEn)

	def genLevel(self,levelsize,screen):
		self.levelList=[]
		random.seed()
		## Create the first 2 platforms manually
		blockTemp = Levelplat(screen,1,200,12,0)
		self.levelList.append(blockTemp)
		blockTemp = Levelplat(screen,0,530,2,0)
		self.levelList.append(blockTemp)
		## Load the first platform
		self.levelList[0].loadPlatform(screen)
		i=2
		while i<levelsize:
			## Generate a random height based on the height from 2 platforms ago
			yRan = self.levelList[i-2].y+random.randint(-100,100)
			if yRan < 200:
				yRan += 100
			elif yRan > 430:
				yRan -= 100
			## Create next platform
			blockTemp = Levelplat(screen,0,yRan,random.randint(8,12),random.randint(0,4))
			self.levelList.append(blockTemp)
			## Every other platform is 530 heigh, and partly based on score.
			blockTemp = Levelplat(screen,0,530,random.randint(2+min(self.score/1000,2),4+min(self.score/500,3)),0)
			self.levelList.append(blockTemp)
			i+=2
		## !!! Not sure what this does
		xRange=0
		for i in range(5):
			self.levelList[i].x = xRange
			self.levelList[i].loadPlatform(screen)
			xRange+=self.levelList[i].size*64

	def drawBlocksOnScreen(self,screen):
		## Remove a level when it falls totaly off the screen
		if (self.levelList[0].x+self.levelList[0].size*64) < 0:
			## Enemies
			self.levelList[0].enemyList=[]
			## !!! Again, not sure
			self.levelList.pop(0)
			self.levelList[4].loadPlatform(screen)
			xRange = 0
			for i in range(4):
				xRange+=self.levelList[i].size*64
			self.levelList[4].x=xRange
		## Draw the blocks onscreen, then move them
		for i in range(5):
			self.levelList[i].drawBlocks(screen)
			self.levelList[i].moveBlocks(self.speed)

	def bulletCollide(self):
		## For every bullet in the air
		for i in self.character.bulletList:
			for j in range(5):
				## With every enemy in the level
				for k in self.levelList[j].enemyList:
					## If they collide
					if i.rect1.colliderect(k.rect1):
						## !!! Why is this test necessary
						if len(self.character.bulletList)>0:
							## Remove the bullet
							self.character.bulletList.remove(i)
						## Kill the enemy
						k.isDead = True
						k.kill()
						self.score+=50

	def playerCollide(self):
		for i in range(5):
			## For all the enemis
			for j in self.levelList[i].enemyList:
				## If they collide with the player
				if j.rect1.colliderect(self.character.rect1):
					## Kill the enemy
					j.isDead = True
					j.kill()
					## Kill (or Injure) the player
					self.playerDeath()
	
	def playerFall(self):
		for i in range(5):
			if self.levelList[i].x > self.character.currentX+self.character.charImage.get_width():
				if self.levelList[i-1].y>480 and self.character.currentY > self.levelList[i].y:
					self.playerDeath()
				break

	def playerDeath(self):
		## Don't kill the player if they are invulnerable due to being hit
		if not self.character.isInvuln and self.character.lives>0:
			## Slow down, become invulnerable, jump to top of screen remove life
			self.speed=4
			self.character.isInvuln=True
			self.character.currentY = 20
			self.character.lives-=1
		elif not self.character.isInvuln:
			## Game over
			print "YOU LOST"
			self.isGame=False
