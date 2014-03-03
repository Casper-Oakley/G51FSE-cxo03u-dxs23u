import pygame,random
from player import Character

class World:
	currentX=0
	currentY=0
	enemy1List=[]

	def __init__(self,screen):
		self.loadLevel(screen)

	def loadLevel(self, screen):
		self.backgroundImage=pygame.image.load("../assets/images/world/Pleiades_large.jpg")
		self.character = Character()
		self.drawLevel(screen)

	def drawLevel(self, screen):
		screen.blit(self.backgroundImage,(self.currentX, self.currentY))
		for i in range(len(self.enemy1List)):
			self.enemy1List[i].move()
			self.enemy1List[i].draw(screen)
		self.character.draw(screen)

	def worldUpdate(self):
		self.scroll()

	def scroll(self):
		self.currentX-=1

	def genEnemy1(self,screen):
		random.seed()
		tempEn = Enemy1(random.randInt(0,640),random.randInt(0,480),screen)
		self.enemy1List.append(tempEn)
