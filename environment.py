import pygame
import sys
import random

class Environment:
	def __init__(self, screenSizeX, screenSizeY):
		pygame.init()
		self.screenSizeX = screenSizeX
		self.screenSizeY = screenSizeY
		self.screen = pygame.display.set_mode((self.screenSizeX, self.screenSizeY))
		self.screen.fill((255,255,255))
		self.numObstacles = random.randint(0, 5)
		self.obsPositions = []
		self.defineStartAndEndPoints()
		for i in range(0, self.numObstacles):
			self.addObstacle()

	def addObstacle(self):
		x = random.randint(int((1/3.0) * self.screenSizeX), int((2/3.0) * self.screenSizeX - 1))
		y = random.randint(0, int(self.screenSizeY - 1))
		self.obsPositions.append((x,y))
		return x, y

	def defineStartAndEndPoints(self):
		self.startX = random.randint(0, int((1/3.0) * self.screenSizeX))
		self.startY = random.randint(0, int(self.screenSizeY))
		self.endX = random.randint(int((2/3.0) * self.screenSizeX), self.screenSizeX)
		self.endY = random.randint(0, int(self.screenSizeY))

	def redrawEnv(self, population):
		self.screen.fill((255,255,255))
		color = (0, 255, 0)
		pygame.draw.circle(self.screen, color, (self.startX, self.startY), 15, 0)
		pygame.draw.circle(self.screen, color, (self.endX, self.endY), 15, 0)
		color = (255, 0, 0)
		for obs in self.obsPositions:
			pygame.draw.circle(self.screen, color, obs, 15, 0)
		color = (0, 0, 255)
		for sample in population.samples:
			pygame.draw.rect(self.screen, color, (sample.x, sample.y, 5, 5), 0)
		pygame.display.update()
			
	def checkExited(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
