import pygame
import sys
import random

screenSizeX = 640
screenSizeY = 480

class environment:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((screenSizeX, screenSizeY))
		pygame.display.update()
		self.screen.fill((255,255,255))

	def addObsticle(self):
		color = (255,0,0)
		x = random.randint(int((1/3.0) * screenSizeX), int((2/3.0) * screenSizeX - 1))
		y = random.randint(0, int(screenSizeY - 1))
		pygame.draw.circle(self.screen, color, (x,y), 15, 0)		
		return x, y
	def startAndEndPoints(self):
		color = (0, 255, 0)
		x1 = random.randint(0, int((1/3.0) * screenSizeX))
		y1 = random.randint(0, int(screenSizeY))
		pygame.draw.circle(self.screen, color, (x1,y1), 15, 0)
		x2 = random.randint(int((2/3.0) * screenSizeX), screenSizeX)
		y2 = random.randint(0, int(screenSizeY))
		pygame.draw.circle(self.screen, color, (x2,y2), 15, 0)
		return x1, y1, x2, y2
	
e = environment()
e.startAndEndPoints()
e.addObsticle()
e.addObsticle()
while(True):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#todo clean the screen



	#calculate the best sample in generation


	#populate best samples for next generation


	#update the screen
	pygame.display.update()
