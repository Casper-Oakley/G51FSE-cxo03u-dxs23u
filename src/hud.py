import pygame

class Hud:

	def drawScore(self,screen,score):
		scoreText=pygame.font.SysFont("helvetica",20,True,False)
		screen.blit(scoreText.render("score: "+str(score),1,(0,0,0)) ,(10,10))

	def drawLife(self,screen,lives):
		print "wat"

	def drawHUD(self,screen,score):
		self.drawScore(screen,score)
