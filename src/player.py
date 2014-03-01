import pygame
import math
from pygame.locals import *

class Character:
	currentX=80
	currentY=0
	gravity = 0.5
	vSpeed = 0
	ammoAmount = 0
	ammoType = "normal"

	angle = 0

	def __init__(self):
		self.loadChar()
	def loadChar(self):
		self.charImage=pygame.image.load("../assets/images/character/charRen1a.png")
		self.charArmImageMaster=pygame.image.load("../assets/images/character/charArm1.png") 
		self.charArmImageRot = self.charArmImageMaster
	def draw(self,screen):
		self.applyGravity()
		self.aimAndDrawArm(screen)
		screen.blit(self.charImage,(self.currentX,self.currentY))
	def applyGravity(self):
		if self.currentY>200:
			self.currentY=200
			self.vSpeed = 0
			self.isJump = False
		else:
			self.vSpeed += self.gravity
			self.currentY += self.vSpeed
	
	def jump(self):
		if self.isJump == False:
			self.vSpeed = -20
			self.isJump = True
	def keyPress(self,key):
		if key[K_w] == 1:
			self.jump()
	def aimAndDrawArm(self,screen):
		self.angle+=1
		self.charArmImageRot = pygame.transform.rotate(self.charArmImageMaster,self.angle)
		self.ab = 48*(math.cos(math.radians(self.angle))+math.sin(math.radians(self.angle)))-48
		screen.blit(self.charArmImageRot,(self.currentX+60-self.ab, self.currentY+60-self.ab))



