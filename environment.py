import pygame
import sys
import random

class environment:
	def __init__(self, screenSizeX, screenSizeY):
		pygame.init()
		self.screenSizeX = screenSizeX
		self.screenSizeY = screenSizeY
		self.screen = pygame.display.set_mode((self.screenSizeX, self.screenSizeY))
		pygame.display.update()
		self.screen.fill((255,255,255))
		self.numObstacles = 0
		self.obsPositions = []
		self.startX = 0
		self.startY = 0
		self.endX = 0
		self.endY = 0
		self.startAndEndPoints()

	def addObstacle(self):
		color = (255,0,0)
		x = random.randint(int((1/3.0) * self.screenSizeX), int((2/3.0) * self.screenSizeX - 1))
		y = random.randint(0, int(self.screenSizeY - 1))
		pygame.draw.circle(self.screen, color, (x,y), 15, 0)
		self.numObstacles = self.numObstacles + 1 
		self.obsPositions.append([x,y])
		return x, y

	def startAndEndPoints(self):
		color = (0, 255, 0)
		self.startX = random.randint(0, int((1/3.0) * self.screenSizeX))
		self.startY = random.randint(0, int(self.screenSizeY))
		pygame.draw.circle(self.screen, color, (self.startX, self.startY), 15, 0)
		self.endX = random.randint(int((2/3.0) * self.screenSizeX), self.screenSizeX)
		self.endY = random.randint(0, int(self.screenSizeY))
		pygame.draw.circle(self.screen, color, (self.endX, self.endY), 15, 0)
		#return x1, y1, x2, y2

	def redrawEnv(self):
		self.screen.fill((255,255,255))
		color = (0, 255, 0)
		pygame.draw.circle(self.screen, color, (self.startX, self.startY), 15, 0)
		pygame.draw.circle(self.screen, color, (self.endX, self.endY), 15, 0)
		color = (255, 0, 0)
		for obs in self.obsPositions:
			pygame.draw.circle(self.screen, color, (obs[0], obs[1]), 15, 0)
	
class sampleInPop:
	def __init__(self, startX, startY, screen):
		self.x = startX
		self.y = startY
		self.moveList = []
		self.screen = screen

	def displaySample(self):
		color = (0, 0, 255)
		pygame.draw.rect(self.screen, color, (self.x, self.y, 5, 5), 0)

	def moveSample(self):
		#randomly move in a given direction
		self.x = self.x + random.randint(-2, 2) 
		self.y = self.x + random.randint(-2, 2)
		self.displaySample()
		self.moveList.append([self.x, self.y])	

	def distToEnd(self, endX, endY):
		self.distanceToEnd = sqrt((self.x - endX)**2 + (self.y - endY)**2)

	def obsticleHit(self, env):
		for obs in env.obsPositions:
			if(abs(self.x - obs[0]) < 5 and abs(self.y - obs[1]) < 5):
				return True
		return False

	def endPointFound(self, env):
		return (abs(self.x - env.endX) < 5 and abs(self.y - env.endY) < 5)


#Main Program
e = environment(640, 480)
e.addObstacle()
e.addObstacle()

#generate first generation
currentGeneration = 1
generation = 1
populationSize = 100
newMovesPerPopulation = 10
populationSamples = []

#create first population
for i in range(0, populationSize):
	populationSamples.append(sampleInPop(e.startX, e.startY, e.screen))
pygame.display.update()

while(True):
	# check if game was exited
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# check if a sample found the end
	for sample in populationSamples:
		if(sample.endPointFound):
			print("AI reached the end")
			break
	
	for i in range(0, newMovesPerPopulation):
		#e.redrawEnv()
		for sample in populationSamples:
			#randomly generate new sample locations until limit of newMovesPerPopulation is reached	
			sample.moveSample()
		pygame.display.update()

	# todo remove samples that hit obstacles

	# todo
	bestSamples = []
	#calculate the best sample in generation
	#sort samples with shortest distances to end first
	#for sample in populationSamples:
		#sort

	#populate best samples for next generation
	generation = generation + 1
	populationSamples = []
	print("Generation: " + str(generation))
	#for samples in bestSamples:
		#make a shallow (non aliased) copy of sample and add both the original and copy to populationSamples
	
	# rerun simulation with all previously moved points of successful samples
	for sample in populationSamples:
		for move in sample.moveList:
			#e.redrawEnv()
			sample.x = move[0]
			sample.y = move[1]
			sample.displaySample()
			pygame.display.update()
