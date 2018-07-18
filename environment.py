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
	def startAndEnd(self):
		color = (0, 255, 0)
		x = random.randint(0, int((1/3.0) * screenSizeX))
		y = random.randint(0, int(screenSizeY))

e = environment()
e.addObsticle()
e.addObsticle()
for event in pygame.event.get():
	if event.type == pygame.QUIT:
		pygame.quit()
		sys.exit()
	pygame.display.update()
