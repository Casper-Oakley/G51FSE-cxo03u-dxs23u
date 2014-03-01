import pygame

class Character:
	currentX=80
	currentY=0
	gravity = 0.5
	vSpeed = 0

	def __init__(self):
		self.loadChar()
	def loadChar(self):
		self.charImage=pygame.image.load("../assets/images/char.jpg")
	def draw(self,screen):
		self.jump()
		screen.blit(self.charImage,(self.currentX,self.currentY))
	def jump(self):
		if self.currentY>200:
			self.currentY=200
		else:
			self.vSpeed += self.gravity
			self.currentY+=self.vSpeed
