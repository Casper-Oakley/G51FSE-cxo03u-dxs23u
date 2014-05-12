import pygame
from pygame.locals import *
from button import Button

class Highscores:

	def __init__(self):
		self.background=pygame.image.load("../assets/images/menu/menuBackground.png")
		self.backButton=Button(200,400,"../assets/images/menu/backButton.png","../assets/images/menu/backButtonHighlight.png")
		self.backButton.isHighlight=True
		highscoreFile = open("../highscores.txt","r")
		self.highscoreStore = []
		self.counter = 0
		for line in highscoreFile:
			self.highscoreStore.append(line)
			self.counter += 1

	def drawMenu(self,screen):
		pygame.draw.rect(screen,(0,0,0),(0,0,640,480))		
		screen.blit(self.background,(0,0))
		self.backButton.drawButton(screen)
		for i in range(self.counter):
			self.drawScore(screen,i,self.highscoreStore[i])

	def drawScore(self,screen,index,score):
		scoreText=pygame.font.SysFont("Helvetica",20,True,False)
		screen.blit(scoreText.render(str(index)+") "+score[:-1],1,(255,0,0)) ,(10,10+index*30))
