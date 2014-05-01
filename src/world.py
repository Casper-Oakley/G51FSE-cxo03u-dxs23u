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
		## Standard image loading
		self.backgroundImage=pygame.image.load("../assets/images/world/iceBackground.png").convert()
		self.baseBackgroundImage=pygame.image.load(
		"../assets/images/world/iceBackgroundBase.png").convert()
		## Create level, character
		self.genLevel(500,screen)
		self.character = Character()
		## Draw the level once
		self.drawLevel(screen)

#function to draw level inc contents
	def drawLevel(self, screen):
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

#main world loop to compute all actions done in frame
	def worldUpdate(self):
		## Moves itself backwards to simulate the 
		## character running forwars against the screen
		self.currentX-=3
		## Loop background around
		if self.currentX < -4000:#is completely off screen
			self.currentX = 640
		## Check for collisions
		self.bulletCollide()
		self.playerCollide()
		## Move the player, update score and increase speed
		self.playerFall()
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
		self.score+=1
		self.speed+=0.01

#generate an enemy and store it in the enemy list
	def genEnemy1(self,screen,x,y):
		## create an enemy1 (snowman)
		tempEn = Enemy1(x,y,screen)
		self.enemy1List.append(tempEn)

##generate the initial level blocks locations and store them
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
#loop to find appropriate heights for each level block
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
#load the first set of blocks inc assets
		for i in range(5):
			self.levelList[i].x = xRange
			self.levelList[i].loadPlatform(screen)
			xRange+=self.levelList[i].size*64

#draw the level blocks, including removing old ones and loading new ones
	def drawBlocksOnScreen(self,screen):
		## Remove a level when it falls totaly off the screen and adds a new one on
		if (self.levelList[0].x+self.levelList[0].size*64) < 0:
			## Enemies
			self.levelList[0].enemyList=[]
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

#for each bullet, tests if it has hit any of the enemies. If it has, kill them and add score.
	def bulletCollide(self):
		## For every bullet in the air
		for i in self.character.bulletList:
			for j in range(5):
				## With every enemy in the level
				for k in self.levelList[j].enemyList:
					if i.bulletRectangle.colliderect(k.enemyRectangle):
					## If they collide
						## Remove the bullet
						self.character.bulletList.remove(i)
						## Kill the enemy
						k.isDead = True
						k.kill()
						self.score+=50

#test if the player has collided with an enemy
	def playerCollide(self):
		for i in range(5):
			## For all the enemis
			for j in self.levelList[i].enemyList:
				if j.enemyRectangle.colliderect(self.character.charRectangle):
				## If they collide with the player
					## Kill the enemy
					j.isDead = True
					j.kill()
					## Kill (or Injure) the player
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
		## Don't kill the player if they are invulnerable due to being hit
		if not self.character.isInvuln and self.character.lives>0:
			## Slow down, become invulnerable, jump to top of screen remove life
			self.speed=8
			self.character.isInvuln=True
			self.character.currentY = 20
			self.character.lives-=1
		elif not self.character.isInvuln:
			self.isGame=False
