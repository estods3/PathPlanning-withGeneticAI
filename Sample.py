import pygame
import random

class Sample:
	def __init__(self, startX, startY, endX, endY):
		self.x, self.y = (startX, startY)
		self.goalX, self.goalY = (endX, endY)
		self.moveList = []
		self.fitness = 10000
		self.isAlive = True
		self.reachedEnd = False

	def moveSample(self):
		if(self.isAlive):
			#randomly move in a given direction
			self.x = self.x + random.randint(-30, 30)
			self.y = self.x + random.randint(-30, 30)
			self.moveList.append([self.x, self.y])	

	def calculateFitness(self):
		self.fitness = 1/16 + 1000/sqrt((self.x - self.goalX)**2 + (self.y - self.goalY)**2)

	def obsticleOrWallHit(self, env):
		for obs in env.obsPositions:
			if(abs(self.x - obs[0]) < 5 and abs(self.y - obs[1]) < 5):
				self.isAlive = False
		if(self.x < 2 or self.y < 2 or self.x == env.screenSizeX - 1 or self.y == env.screenSizeY - 1):
			self.isAlive = False

	def endPointFound(self, env):
		self.reachedEnd = (abs(self.x - env.endX) < 5 and abs(self.y - env.endY) < 5)
		self.isAlive = False
	
	#todo
	#def clone():
	
	
	#todo
	#def mutate():