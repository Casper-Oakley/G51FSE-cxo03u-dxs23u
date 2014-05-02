import pygame
import math
from bullet import Bullet
from pygame.locals import *

class Character:
	currentX=80
	currentY=0
	gravity = 1.6
	vSpeed = 0
	ammoAmount = 0
	ammoType = "normal"
	bulletList = []
	animIndex = 0
	lives=3
	invulnTimer=0
	isInvuln=False
	isJump = True

	angle = 0

	def __init__(self):
		self.loadChar()

	def loadChar(self):
		## Load all the images for the characters run cycle
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
		## Initialise the animated sprite
		self.charImage=self.charRunCycleList[0]
		## load the arm. This arm is never rotated to maintain image quality.
		self.charArmImageMaster=pygame.image.load("../assets/images/character/charArm2.png").convert_alpha()
		## Initialise the arm which is rotaated on the fly.
		self.charArmImageRot = self.charArmImageMaster
		## Set collision box
		self.rect1 = pygame.Rect(self.currentX,self.currentY,self.charImage.get_width(),self.charImage.get_height())
		
		## Sounds
		self.laserSound = pygame.mixer.Sound("../assets/sounds/effects/laser.wav")
		self.jumpSound = pygame.mixer.Sound("../assets/sounds/effects/jump.wav")
		self.landSound = pygame.mixer.Sound("../assets/sounds/effects/land.wav")

	def draw(self,screen):
		## Update bullet list and draw bullets.
		self.deleteOffscreenBullets()
		#self.aimAndDrawArm(screen)
		for i in range(len(self.bulletList)):
			self.bulletList[i].move()
			self.bulletList[i].draw(screen)
		## Update animation.
		self.animIndex = (self.animIndex+1)%len(self.charRunCycleList) 
		self.charImage = self.charRunCycleList[self.animIndex]
		## Update the arm.
		self.aimAndDrawArm(screen)
		## Draw the character. If the character is invulnerable, draw it blinking.
		if not self.isInvuln:
			screen.blit(self.charImage,(self.currentX,self.currentY))
		elif self.invulnTimer%16<8 and self.isInvuln:
			screen.blit(self.charImage,(self.currentX,self.currentY))
			self.invulnTimer+=1
		else:
			self.invulnTimer+=1
		## After aperiod of blinking, stop and become vunerable.
		if self.invulnTimer > 60 and self.isInvuln:
			self.isInvuln=False
			self.invulnTimer=0
		

	def applyGravity(self,currentLow):
		## if character is below the floor
		if self.currentY > ( currentLow - self.charImage.get_height() ):
			if (self.isJump == True):
				## Sound effects
				self.landSound.play()
			## snap the character to the floor
			self.currentY=currentLow-self.charImage.get_height()
			## reset jumping and vspeed
			self.vSpeed = 0
			self.isJump = False
		else:
			## otherwise, fall down
			self.vSpeed += self.gravity
			self.currentY += self.vSpeed
			self.rect1.y = self.currentY
	
	def jump(self):
		## Jump if not in the air.
		if self.isJump == False:
			self.vSpeed = -24
			self.isJump = True
			## Sound effects
			self.jumpSound.play()

	## Activate jumping.
	def keyPress(self,key):
		if key[K_w] == 1:
			self.jump()

	def aimAndDrawArm(self,screen):
		## Set the rotation angle based on mouse position
		self.angle=-math.degrees(math.atan2((pygame.mouse.get_pos()[1]-self.currentY-64),(pygame.mouse.get_pos()[0]-self.currentX-64)))
		## Rotate the arm image
		self.charArmImageRot = pygame.transform.rotate(self.charArmImageMaster,self.angle)
		## perform some rather unpleasant maths to make the arm rotate around the characters shoulder properly.
		self.ab = (72*(math.cos(math.radians(self.angle%90))+math.sin(math.radians(self.angle%90))))-72
		#xOffset = self.currentX+35-self.ab+30*math.cos(math.radians(-self.angle))
		#yOffset = self.currentY+40-self.ab+30*math.sin(math.radians(-self.angle))
		xOffset = -self.ab+1*math.cos(math.radians(-self.angle))+4
		yOffset = -self.ab+1*math.sin(math.radians(-self.angle))-14
		## draw the rotated arm image in position
		screen.blit(self.charArmImageRot,(self.currentX+xOffset,self.currentY+yOffset))
		
	def shoot(self,screen):
		## create a new bullet based on the current angle of the arm. currently does not fire from gun.
		self.ab = 0#(72*(math.cos(math.radians(self.angle%90))+math.sin(math.radians(self.angle%90))))-72
		xOff = 42*math.cos(math.radians(-self.angle))+64+5
		yOff = 42*math.sin(math.radians(-self.angle))+64-15
		tempBullet = Bullet(self.currentX+xOff,self.currentY+yOff,-self.angle,screen)
		## add the bullet to the list.
		self.bulletList.append(tempBullet)
		## Play the bullet shoot sound
		self.laserSound.play()
	
	## activate shooting.
	def mousePress(self,key,screen):
		if key[0] == 1:
			self.shoot(screen)

	def deleteOffscreenBullets(self):
		## for each bullet
		for i in self.bulletList:
			## if its not on screen
			if i.x > 640 or i.x < 0 or i.y > 480 or i.y < 0:
				## remove it form the bullet list.
				self.bulletList.remove(i)
