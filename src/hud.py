import pygame

class Hud:

	def drawScore(self,screen,score):
		scoreText=pygame.font.SysFont("Helvetica",20,True,False)
		screen.blit(scoreText.render("score: "+str(score),1,(0,0,0)) ,(10,10))

	def drawLife(self,screen,lives):
		for i in range(lives):
			screen.blit(self.lifeImage,(i*48+496,10))

	def drawHUD(self,screen,score,lives):
		self.drawScore(screen,score)
		self.drawLife(screen,lives)

	def loadHUD(self,screen):
		self.lifeImage=pygame.image.load("../assets/images/character/heartIcon.png").convert_alpha()

#draws restart message
	def restart(self,screen,score):
		pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
		gameOver=pygame.font.SysFont("Helvetica",20,True,False)
		restartText=pygame.font.SysFont("Helvetica",24,True,False)
		screen.blit(gameOver.render("Game over! You earnt:"+str(score),1,(255,255,255)),(200,180))
		screen.blit(restartText.render("Press space to continue",1,(255,30,30)),(200,230))
