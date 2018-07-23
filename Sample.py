import pygame
import random
import math
import numpy as np

##---------------------------------------------------------------------------------------------------------
## Sample: A Sample of a Population. A Sample only knows where it starts and where the end is
## the Sample has Genetics (random decision-making) and PointMassKinematics (to move about the Environment)
##---------------------------------------------------------------------------------------------------------
class Sample:
	def __init__(self, startX, startY, endX, endY):
		self.pathFound = False
		self.startX, self.startY = (startX, startY)
		self.color = (0, 0, 255)
		
		#Kinematics
		self.kinematics = PointMassKinematics(startX, startY)
		self.endPoint = Vector(endX, endY) #does this need to be known by a sample? its the same for all samples in a pop
		
		#Genetic Attributes & Decision Making
		self.fitness = 0
		self.genetics = Genetics(1000)

	def move(self):
		if(self.kinematics.isAlive):
			if(len(self.genetics.directions) > self.genetics.step):
				#randomly move in a given direction
				self.kinematics.a = self.genetics.directions[self.genetics.step]
				self.genetics.step = self.genetics.step + 1
			else:
				self.kinematics.isAlive = False
			self.kinematics.accelerate()

	def calculateFitness(self):
		if(self.pathFound):
			self.fitness = 1/16 + 10000/(self.genetics.step * self.genetics.step) #todo
		else:
			self.fitness = 1.0/((self.kinematics.p.x - self.endPoint.x)**2 + (self.kinematics.p.y - self.endPoint.y)**2)
	
	def procreate(self):
		baby = Sample(self.startX, self.startY, self.endPoint.x, self.endPoint.y);
		baby.genetics = self.genetics.clone()
		return baby;

##---------------------------------------------------------------------------
## Point Mass Kinematics: Models how a Sample interacts with it's Environment
##---------------------------------------------------------------------------
class PointMassKinematics:
	def __init__(self, startX, startY):
		self.isAlive = True
		self.p = Vector(startX, startY)
		self.v = Vector(0, 0)
		self.a = Vector(0, 0)
		
	def obstacleHit(self, obstacleOrigin, obstacleRadius):
		if(self.p.distanceToPoint(obstacleOrigin) < obstacleRadius):
			self.isAlive = False
				
	def wallHit(self, wallX, wallY):
		buffer = 5
		if((self.p.x < buffer or self.p.x > (wallX - buffer)) or (self.p.y < buffer or self.p.y > (wallY - buffer))):
			self.isAlive = False
			
	def endPointFound(self, endPoint):
		endPointSize = 15 #todo make field in Environment
		self.pathFound = (self.p.distanceToPoint(endPoint) < endPointSize)
		if(self.pathFound):
			self.isAlive = False
	
	def accelerate(self):
		self.v.add(self.a)
		if (self.v.magnitude() > 5):
			self.v = Vector(self.v.x / self.v.magnitude(), self.v.y / self.v.magnitude())
		self.p.add(self.v)

##--------------------------------------------------------------------
## Vector: Used to represent points, velocities, and accelerations for 
## Samples, obstacles, and start/end points
##--------------------------------------------------------------------
class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def add(self, p):
		self.x = self.x + p.x
		self.y = self.y + p.y
	
	def magnitude(self):
		return math.sqrt((self.x)**2 + (self.y)**2)

	def distanceToPoint(self, p):
		return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

##----------------------------------------------------------------------------
## Genetics: Decision-making "genes" assigned at birth (__init__) for a Sample
##----------------------------------------------------------------------------
class Genetics:
	def __init__(self, size):
		self.step = 0;
		self.directions = []
		self.randomize(size)

	def randomize(self, size):
		for i in range(size):
			f = random.random() * (2*3.14159)
			self.directions.append(Vector(math.cos(f), math.sin(f)))

	def clone(self):
		c = Genetics(len(self.directions))
		c.directions = []
		mutationRate = 0.1 #unit: % def: chance that any vector in directions gets changed
		for direction in self.directions:
			f = random.random()
			if (f < mutationRate):
				f = random.random() * (2*3.14159)
				c.directions.append(Vector(math.cos(f), math.sin(f)))
			else:
				c.directions.append(direction)
		return c;