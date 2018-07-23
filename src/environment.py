import pygame
import sys
import random
from Sample import Vector

##--------------------------------------------------------------------------------------------
## Environment: initializes 'pygame' environment and start, end, and obstacle positions
## controls all redrawing of the pygame interface
##--------------------------------------------------------------------------------------------
class Environment:
	def __init__(self, screenWidth, screenHeight):
		pygame.init()
		self.screenSizeX, self.screenSizeY = screenWidth, screenHeight
		self.screen = pygame.display.set_mode((self.screenSizeX, self.screenSizeY))
		self.screen.fill((255,255,255))
		self.numObstacles = random.randint(8, 13)
		self.obstacles = []
		#todo use Vector() class to define start and end points
		self.defineStartAndEndPoints()
		for i in range(0, self.numObstacles):
			self.addObstacle()

	def addObstacle(self):
		x = random.randint(int((1/5.0) * self.screenSizeX), int((4/5.0) * self.screenSizeX - 1))
		y = random.randint(0, int(self.screenSizeY - 1))
		size = random.randint(15, 40)
		self.obstacles.append([Vector(x, y), size])
		return x, y

	def defineStartAndEndPoints(self):
		self.startX = random.randint(0, int((1/5.0) * self.screenSizeX))
		self.startY = random.randint(int(self.screenSizeY * 0.2), int(self.screenSizeY * 0.8))
		self.endX = random.randint(int((4/5.0) * self.screenSizeX), self.screenSizeX)
		self.endY = random.randint(int(self.screenSizeY * 0.2), int(self.screenSizeY * 0.8))
		self.linePoints = [(self.startX, self.startY)]
		
	def redrawEnv(self, population):
		self.screen.fill((255,255,255))
		pygame.font.init()
		myfont = pygame.font.SysFont('Comic Sans MS', 20)
		textsurface = myfont.render('Generation: ' + str(population.generation), False, (0, 0, 0))
		self.screen.blit(textsurface,(0,0))
		color = (0, 200, 0)
		pygame.draw.circle(self.screen, color, (self.startX, self.startY), 15, 0)
		pygame.draw.circle(self.screen, color, (self.endX, self.endY), 15, 0)
		color = (200, 0, 0)
		for obs in self.obstacles:
			obsOrigin, size = obs
			pygame.draw.circle(self.screen, color, (obsOrigin.x, obsOrigin.y), size, 0)
		for sample in population.samples:
			pygame.draw.rect(self.screen, sample.color, (sample.kinematics.p.x, sample.kinematics.p.y, 5, 5), 0)
			if(sample.isBest):
				self.linePoints.append((sample.kinematics.p.x, sample.kinematics.p.y))
				pygame.draw.lines(self.screen, (0, 0, 200), False, self.linePoints, 3)	
		pygame.display.update()
		
	def clearPath(self):
		self.linePoints = [(self.startX, self.startY)]
		
	def checkExited(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()