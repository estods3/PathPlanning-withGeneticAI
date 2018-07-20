import pygame
import random
import math
import numpy as np

class Sample:
	def __init__(self, startX, startY, endX, endY):
		
		self.isAlive = True
		self.reachedEnd = False
		self.startX, self.startY = (startX, startY)
		self.endX, self.endY = (endX, endY)
		
		#Kinematics
		#todo make a point class: p.x, p.y, p.add, p.color
		self.p = np.array((self.startX, self.startY))
		self.v = np.array((0, 0))
		self.a = np.array((0, 0))
				
		#Genetic Attributes & Decision Making
		self.fitness = 0
		self.genetics = genetics(1000)

	def moveSample(self):
		if(self.isAlive):
			if(len(self.genetics.directions) > self.genetics.step):
				#randomly move in a given direction
				self.a = self.genetics.directions[self.genetics.step]
				self.genetics.step = self.genetics.step + 1
			else:
				self.isAlive = False
			self.v = np.add(self.v, self.a)
			if (np.linalg.norm(self.v) > 3):
				self.v = self.v / (np.linalg.norm(self.v))
			self.p = np.add(self.p,self.v)

	def calculateFitness(self):
		if(self.reachedEnd):
			#todo
			self.fitness = 1/16 + 1000/(1)
		else:
			self.fitness = 1.0/((self.p[0]- self.endX)**2 + (self.p[1] - self.endY)**2)
			
	def obsticleOrWallHit(self, env):
		for obs in env.obsPositions:
			if(abs(self.p[0] - obs[0]) < 15 and abs(self.p[1] - obs[1]) < 15):
				self.isAlive = False
		#todo if start point is too close to a wall this could cause an error
		if(self.p[0] < 5 or self.p[1] < 5 or self.p[0] > env.screenSizeX - 5 or self.p[1] > env.screenSizeY - 5):
			self.isAlive = False

	def endPointFound(self, env):
		self.reachedEnd = (abs(self.p[0] - env.endX) < 15 and abs(self.p[1] - env.endY) < 15)
		if(self.reachedEnd):
			self.isAlive = False
	
	def procreate(self):
		baby = Sample(self.startX, self.startY, self.endX, self.endY);
		baby.genetics = self.genetics.clone()
		return baby;
	
	
class genetics:
	def __init__(self, size):
		self.step = 0;
		self.directions = [];
		self.randomize(size);

	def randomize(self, size):
		for i in range(0, size):
			f = random.random() * (2*3.14159);
			self.directions.append(np.array((math.cos(f), math.sin(f))))

	def clone(self):
		c = genetics(len(self.directions))
		c.directions = []
		for direction in self.directions:
			c.directions.append(direction)

		return c;

	def mutate(self):
		mutationRate = 0.01 #chance that any vector in directions gets changed
		for direction in self.directions:
			f = random.random()
			if (f < mutationRate):
				f = random.random() * (2*3.14159);
				direction = [math.cos(f), math.sin(f)]