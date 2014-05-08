import pygame
from pygame.locals import *
from button import Button

class Menu:

	def __init__(self):
		self.playButton=Button(200,200,"../assets/images/menu/playButton.png","../assets/images/menu/playButton.png")
		self.optionsButton=Button(200,300,"../assets/images/menu/optionsButton.png","../assets/images/menu/optionsButton.png")
		self.highScoresButton=Button(200,400,"../assets/images/menu/highScoresButton.png","../assets/images/menu/highScoresButton.png")

	def drawMenu(self,screen):
		self.playButton.drawButton(screen)
		self.optionsButton.drawButton(screen)
		self.highScoresButton.drawButton(screen)
