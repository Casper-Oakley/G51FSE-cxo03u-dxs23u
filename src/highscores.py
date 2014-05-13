import pygame
from pygame.locals import *
from button import Button

class Highscores:

	def __init__(self):
		self.background=pygame.image.load("../assets/images/menu/menuBackground.png")
		self.backButton=Button(256,400,"../assets/images/menu/backButton.png","../assets/images/menu/backButtonHighlight.png")
		self.backButton.isHighlight=True
		##on initiate, read highscores file and store info
		highscoreFile = open("../highscores.txt","r")
		self.highscoreStore = []
		self.counter = 0
		for line in highscoreFile:
			self.highscoreStore.append(line)
			self.counter += 1

	def drawMenu(self,screen):
		pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
		screen.blit(self.background,(0,0))
		highscoreBackground = pygame.Surface((200,340))
		highscoreBackground.fill((255,255,255))
		highscoreBackground.set_alpha(120)
		screen.blit(highscoreBackground,(200,60))
		self.backButton.drawButton(screen)
		for i in range(self.counter):
			self.drawScore(screen,i,self.highscoreStore[i])
		self.drawHighscoreText(screen)

##function to draw highscores onto screen
	def drawScore(self,screen,index,score):
		scoreText=pygame.font.SysFont("verdana",20,True,False)
#print in red the whole line string minus the \n
		screen.blit(scoreText.render(str(index+1)+") "+score[:-1],1,(255,0,0)) ,(200,100+index*30))

##function to add text
	def drawHighscoreText(self,screen):
		highscoreText=pygame.font.SysFont("verdana",20,True,False)
		screen.blit(highscoreText.render("Highscores",1,(255,0,0)),(200,60))
