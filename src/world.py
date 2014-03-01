import pygame
from player import Character

class World:
	currentX=0
	currentY=0

	def __init__(self,background):
		self.backgroundColor=background
		
	def loadLevel(self, screen):
		self.backgroundImage=pygame.image.load("../assets/images/Pleiades_large.jpg")
		self.drawBackground(screen)
		self.character = Character()
	def drawBackground(self, screen):
		screen.fill(self.backgroundColor)
		screen.blit(self.backgroundImage,(self.currentX, self.currentY))
	def worldUpdate(self):
		self.scroll()

	def scroll(self):
		self.currentX-=1
