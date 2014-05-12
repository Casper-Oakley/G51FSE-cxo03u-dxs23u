import pygame
from pygame.locals import *
from button import Button

class Gameover:

	def __init__(self):
		self.playButton=Button(256,300,"../assets/images/menu/playButton.png","../assets/images/menu/playButtonHighlight.png")
		self.highScoresButton=Button(256,400,"../assets/images/menu/highScoresButton.png","../assets/images/menu/highScoresButtonHighlight.png")
		self.selectLocation = 0

	def drawMenu(self,screen,score):
		pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
		if self.selectLocation == 0:
			self.playButton.isHighlight=True
			self.highScoresButton.isHighlight=False
		elif self.selectLocation == 1:
			self.playButton.isHighlight=False
			self.highScoresButton.isHighlight=True
		self.playButton.drawButton(screen)
		self.highScoresButton.drawButton(screen)
		gameOver=pygame.font.SysFont("verdana",20,True,False)
		screen.blit(gameOver.render("Game Over! You Earned: "+str(score),1,(255,255,255)),(160,180))

	def keyPress(self,key):
			if key[K_w] == 1:
				self.selectLocation -= 1
			elif key[K_s] == 1:
				self.selectLocation += 1
			elif key[K_UP] == 1:
				self.selectLocation -= 1
			elif key[K_DOWN] == 1:
				self.selectLocation += 1
			if self.selectLocation > 1:
				self.selectLocation = 0
			elif self.selectLocation < 0:
				self.selectLocation = 1
