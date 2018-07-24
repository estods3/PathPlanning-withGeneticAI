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
		
		#Create Start and End Points
		self.defineStartAndEndPoints()
		
		#Create Obstacles
		self.obstacles = []
		self.numObstacles = random.randint(10, 17)
		for i in range(0, self.numObstacles):
			self.addObstacle()

	# Add obstacles in the middle section of the environment
	def addObstacle(self):
		x = random.randint(int((1/5.0) * self.screenSizeX), int((4/5.0) * self.screenSizeX - 1))
		y = random.randint(0, int(self.screenSizeY - 1))
		size = random.randint(15, 40)
		self.obstacles.append([Vector(x, y), size])
		return x, y

	# Defines start and end points for the environment. each on opposite ends of the screen
	def defineStartAndEndPoints(self):
		x = random.randint(0, int((1/5.0) * self.screenSizeX))
		y = random.randint(int(self.screenSizeY * 0.2), int(self.screenSizeY * 0.8))
		self.linePoints = [(x, y)]
		self.startPoint = Vector(x,y)
		x = random.randint(int((4/5.0) * self.screenSizeX), self.screenSizeX)
		y = random.randint(int(self.screenSizeY * 0.2), int(self.screenSizeY * 0.8))
		self.endPoint = Vector(x,y)
	
	# Redraw the environment with current generation printout, obstacles, samples, and path
	def redrawEnv(self, population):
		self.screen.fill((255,255,255))
		pygame.font.init()
		font = pygame.font.SysFont('Comic Sans MS', 20)
		textsurface = font.render('Generation: ' + str(population.generation), False, (0, 0, 0))
		self.screen.blit(textsurface,(0,0))
		color = (0, 200, 0)
		pygame.draw.circle(self.screen, color, (self.startPoint.x, self.startPoint.y), 15, 0)
		pygame.draw.circle(self.screen, color, (self.endPoint.x, self.endPoint.y), 15, 0)
		color = (200, 0, 0)
		for obs in self.obstacles:
			obsOrigin, size = obs
			pygame.draw.circle(self.screen, color, (obsOrigin.x, obsOrigin.y), size, 0)
		for sample in population.samples:
			pygame.draw.rect(self.screen, sample.color, (sample.kinematics.p.x, sample.kinematics.p.y, 5, 5), 0)
			if(sample.isFittest):
				self.linePoints.append((sample.kinematics.p.x, sample.kinematics.p.y))
				pygame.draw.lines(self.screen, (0, 0, 200), False, self.linePoints, 3)	
		pygame.display.update()
		
	# Clear the path to create a new one for the next generation
	def clearPath(self):
		self.linePoints = [(self.startPoint.x, self.startPoint.y)]
	
	# Check to see if the program was exited
	def checkExited(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()