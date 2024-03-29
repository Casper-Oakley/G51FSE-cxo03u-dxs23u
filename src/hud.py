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

	## Loads the images required by the HUD
	def loadHUD(self,screen):
		self.lifeImage=pygame.image.load("../assets/images/character/heartIcon.png").convert_alpha()
