import pygame
import math
from bullet import Bullet
from pygame.locals import *

class Character:

	def __init__(self):
		self.currentX=80
		self.currentY=0
		self.gravity = 1.6
		self.vSpeed = 0
		self.ammoAmount = 0
		self.ammoType = "normal"
		self.bulletList = []
		self.animIndex = 0
		self.lives=3
		self.invulnTimer=0
		self.isInvuln=False
		self.angle = 0
		self.loadChar()

#loads the images in the animation loop for the character and creates a hitbox
	def loadChar(self):
		self.charRunCycleList = []
		self.charRunCycleList.append(pygame.image.load("../assets/images/character/charRen1a.png").convert_alpha())
		self.charRunCycleList.append(pygame.image.load("../assets/images/character/charRen1b.png").convert_alpha())
		self.charRunCycleList.append(pygame.image.load("../assets/images/character/charRen1c.png").convert_alpha())
		self.charRunCycleList.append(pygame.image.load("../assets/images/character/charRen1d.png").convert_alpha())
		self.charRunCycleList.append(pygame.image.load("../assets/images/character/charRen1e.png").convert_alpha())
		self.charRunCycleList.append(pygame.image.load("../assets/images/character/charRen1f.png").convert_alpha())
		self.charRunCycleList.append(pygame.image.load("../assets/images/character/charRen1e.png").convert_alpha())
		self.charRunCycleList.append(pygame.image.load("../assets/images/character/charRen1d.png").convert_alpha())
		self.charRunCycleList.append(pygame.image.load("../assets/images/character/charRen1c.png").convert_alpha())
		self.charRunCycleList.append(pygame.image.load("../assets/images/character/charRen1b.png").convert_alpha())
		self.charImage=self.charRunCycleList[0]
		self.charArmImageMaster=pygame.image.load("../assets/images/character/charArm2.png").convert_alpha()
		self.charArmImageRot = self.charArmImageMaster
		self.charRectangle = pygame.Rect(self.currentX,self.currentY,self.charImage.get_width(),self.charImage.get_height())

#draws the player and all the bullets onto the screen
	def draw(self,screen):
		self.isBulletOut()
		#self.aimAndDrawArm(screen)
		for i in range(len(self.bulletList)):
			self.bulletList[i].move()
			self.bulletList[i].draw(screen)
		self.charImage = self.charRunCycleList[self.animIndex]
		if not self.isInvuln:
			self.aimAndDrawArm(screen)
			screen.blit(self.charImage,(self.currentX,self.currentY))
		elif self.invulnTimer%16<8 and self.isInvuln:
			self.aimAndDrawArm(screen)
			screen.blit(self.charImage,(self.currentX,self.currentY))
			self.invulnTimer+=1
		else:
			self.invulnTimer+=1
		if self.invulnTimer > 60 and self.isInvuln:
			self.isInvuln=False
			self.invulnTimer=0
		self.animIndex = (self.animIndex+1)%len(self.charRunCycleList)

#moves the character based off gravity, taking into account if jumping
	def applyGravity(self,currentLow):
		if self.currentY>currentLow-self.charImage.get_height():
			self.currentY=currentLow-self.charImage.get_height()
			self.vSpeed = 0
			self.isJump = False
		else:
			self.vSpeed += self.gravity
			self.currentY += self.vSpeed
			self.charRectangle.y=self.currentY
	
#jumps the character
	def jump(self):
		if self.isJump == False:
			self.vSpeed = -24
			self.isJump = True

#recieves input and acts accordingly
	def keyPress(self,key):
		if key[K_w] == 1:
			self.jump()

#draws the arm such that it will face the mouse at it's location
	def aimAndDrawArm(self,screen):
		self.angle=-math.degrees(math.atan2((pygame.mouse.get_pos()[1]-self.currentY-64),(pygame.mouse.get_pos()[0]-self.currentX-64)))
		self.charArmImageRot = pygame.transform.rotate(self.charArmImageMaster,self.angle)
#ab represents the hypotenous
		self.ab = (24*(math.cos(math.radians(self.angle%90))+math.sin(math.radians(self.angle%90))))-24
		xOffset = -self.ab+30*math.cos(math.radians(-self.angle))+35
		yOffset = -self.ab+30*math.sin(math.radians(-self.angle))+40
		screen.blit(self.charArmImageRot,(self.currentX+xOffset,self.currentY+yOffset))

#fires a bullet such that the bullet's start location and angle it moves at is from the arm
	def shoot(self,screen):
		tempBullet = Bullet(self.currentX+30-self.ab+30*math.cos(math.radians(-self.angle)),self.currentY+45-self.ab+30*math.sin(math.radians(-self.angle)),-self.angle,screen)
		self.bulletList.append(tempBullet)

#reads for mouse input
	def mousePress(self,key,screen):
		if key[0] == 1:
			self.shoot(screen)

#removes all bullets that are out of screen
	def isBulletOut(self):
		for i in self.bulletList:
			if i.x > 640 or i.x < 0 or i.y > 480 or i.y < 0:
				self.bulletList.remove(i)
