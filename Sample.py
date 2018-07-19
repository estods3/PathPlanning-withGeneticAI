import pygame
import random
import math

class Sample:
	def __init__(self, startX, startY, endX, endY):
		self.px, self.py = (startX, startY)
		self.vx, self.vy = (0, 0)
		self.ax, self.ay = (0, 0)
		self.startX, self.startY = (startX, startY)
		self.endX, self.endY = (endX, endY)
		
		self.isAlive = True
		self.reachedEnd = False
		
		self.fitness = 0
		self.genetics = genetics(1000)

	def moveSample(self):
		if(self.isAlive):
			if(len(self.genetics.directions) > self.genetics.step):
				#randomly move in a given direction
				self.ax, self.ay = self.genetics.directions[self.genetics.step]
				self.genetics.step = self.genetics.step + 1
			else:
				self.isAlive = False
			self.vx, self.vy = (self.vx + self.ax, self.vy + self.ay)
			self.px, self.py = (self.px + self.vx, self.px + self.vy)

	def calculateFitness(self):
		if(self.reachedEnd):
			#todo
			self.fitness = 1/16 + 1000/(1)
		else:
			self.fitness = 1.0/((self.px - self.endX)**2 + (self.py - self.endY)**2)
			
	def obsticleOrWallHit(self, env):
		for obs in env.obsPositions:
			if(abs(self.px - obs[0]) < 15 and abs(self.py - obs[1]) < 15):
				self.isAlive = False
		#todo if start point is too close to a wall this could cause an error
		if(self.px < 5 or self.py < 5 or self.px > env.screenSizeX - 5 or self.py > env.screenSizeY - 5):
			self.isAlive = False

	def endPointFound(self, env):
		self.reachedEnd = (abs(self.px - env.endX) < 15 and abs(self.py - env.endY) < 15)
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
			self.directions.append([math.cos(f), math.sin(f)])

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