import pygame
from world import World


class Window:
	width=400
	height=400
	background = 0,0,0
	exiting = False
	Clock = pygame.time.Clock()
	def setWindow(self):
		self.screen = pygame.display.set_mode((self.width,self.height))
		self.screen.fill(self.background)
		pygame.key.set_repeat(1,1)
		self.world = World(self.background)
		self.world.loadLevel(self.screen)
	def gameLoop(self):
		while self.exiting == False:
			#for event in pygame.event.get():
				#if event.type == pygame.QUIT:
					#pygame.exit()
				#if event.type == KEYDOWN:
					#key = pygame.key.get_pressed()
					#if key[K_ESCAPE] == 1:
						#print "exiting..."
						#exiting = True
			self.world.worldUpdate()
			self.draw()
			pygame.display.flip()
			self.Clock.tick(120)
			pygame.display.set_caption(str(self.Clock.get_fps()))
		pygame.quit()
	def draw(self):
		self.world.drawBackground(self.screen)
		self.world.character.draw(self.screen)

