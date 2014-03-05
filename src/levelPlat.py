import pygame
from levelblock import Levelblock

class Levelplat:
	x=0
	y=0
	size=0
	platList=[]

	def __init__(self,screen,x,y,size):
		self.x=x
		self.y=y
		self.size=size

	def loadPlatform(self,screen):
		for i in range(self.size):
			blockTemp = Levelblock(self.x+i*64,self.y,2,0,-1)
			self.platList.append(blockTemp)
		for i in self.platList:
			i.load(screen)

	def drawBlocks(self,screen):
		counter = 0
		for i in self.platList:
			i.draw(screen,counter*64+self.x,self.y)
			counter+=1

	def moveBlocks(self):
		self.x-=10
