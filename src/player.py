import pygame
import math
from bullet import Bullet
from pygame.locals import *

class Character:
	currentX=80
	currentY=0
	gravity = 1.0
	vSpeed = 0
	ammoAmount = 0
	ammoType = "normal"
	bulletList = []

	angle = 0

	def __init__(self):
		self.loadChar()

	def loadChar(self):
		self.charImage=pygame.image.load("../assets/images/character/charRen1a.png").convert()
		self.charImage.set_colorkey((255,0,255))
		self.charArmImageMaster=pygame.image.load("../assets/images/character/charArm1.png").convert()
		self.charArmImageMaster.set_colorkey((255,0,255))
		self.charArmImageRot = self.charArmImageMaster

	def draw(self,screen):
		self.applyGravity()
		self.aimAndDrawArm(screen)
		for i in range(len(self.bulletList)):
			self.bulletList[i].move()
			self.bulletList[i].draw(screen)
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
			self.vSpeed = -10
			self.isJump = True

	def keyPress(self,key):
		if key[K_w] == 1:
			self.jump()

	def aimAndDrawArm(self,screen):
		self.angle=-math.degrees(math.atan2((pygame.mouse.get_pos()[1]-self.currentY-64),(pygame.mouse.get_pos()[0]-self.currentX-64)))
		self.charArmImageRot = pygame.transform.rotate(self.charArmImageMaster,self.angle)
		self.ab = (24*(math.cos(math.radians(self.angle%90))+math.sin(math.radians(self.angle%90))))-24
		screen.blit(self.charArmImageRot,(self.currentX+30-self.ab+30*math.cos(math.radians(-self.angle)), self.currentY+45-self.ab+30*math.sin(math.radians(-self.angle))))

	def shoot(self,screen):
		tempBullet = Bullet(self.currentX+30-self.ab+30*math.cos(math.radians(-self.angle)),self.currentY+45-self.ab+30*math.sin(math.radians(-self.angle)),-self.angle,screen)
		self.bulletList.append(tempBullet)

	def mousePress(self,key,screen):
		if key[0] == 1:
			self.shoot(screen)
