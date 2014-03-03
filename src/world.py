import pygame
from player import Character

class World:
	currentX=0
	currentY=0

	def __init__(self,screen):
		self.loadLevel(screen)
	def loadLevel(self, screen):
		self.backgroundImage=pygame.image.load("../assets/images/world/Pleiades_large.jpg")
		self.character = Character()
		self.drawLevel(screen)
	def drawLevel(self, screen):
		screen.blit(self.backgroundImage,(self.currentX, self.currentY))
		self.character.draw(screen)
	def worldUpdate(self):
		self.scroll()

	def scroll(self):
		self.currentX-=1
