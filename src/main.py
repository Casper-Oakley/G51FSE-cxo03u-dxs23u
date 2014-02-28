import pygame
from pygame.locals import *
from random import *
import math

class World:
	currentX=0

	def __init__(self,background):
		self.backgroundColor=background
		
	def loadLevel(self, screen):
		self.backgroundImage=pygame.image.load("../assets/images/Pleiades_large.jpg")
		self.imageRect=self.backgroundImage.get_rect()
		self.drawBackground(screen)
	def drawBackground(self, screen):
		screen.fill(self.backgroundColor)
		screen.blit(self.backgroundImage,self.imageRect)

class Window:
	width=400
	height=400
	background = 0,0,0
	exiting = False
	Clock = pygame.time.Clock()
	def setWindow(self):
		self.screen = pygame.display.set_mode((self.width,self.height))
		self.screen.fill(self.background)
		pygame.key.set_repeat(1,1)
		self.world = World(self.background)
		self.world.loadLevel(self.screen)
	def gameLoop(self):
		while self.exiting == False:
			#for event in pygame.event.get():
				#if event.type == pygame.QUIT:
					#pygame.exit()
				#if event.type == KEYDOWN:
					#key = pygame.key.get_pressed()
					#if key[K_ESCAPE] == 1:
						#print "exiting..."
						#exiting = True
			self.world.drawBackground(self.screen)
			pygame.display.flip()
			self.Clock.tick(120)
			pygame.display.set_caption(str(self.Clock.get_fps()))
		pygame.quit()
		

class Character:
	currentX=80
	currentY=200



def main():
	pygame.init()
	pygame.font.init()
	mainWindow = Window()
	mainWindow.setWindow()
	mainWindow.gameLoop()

main()
