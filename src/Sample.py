import pygame
import random
import math
import numpy as np

##---------------------------------------------------------------------------------------------------------
## Sample: A Sample of a Population. A Sample only knows where it starts and where the end is
## the Sample has Genetics (random decision-making) and PointMassKinematics (to move about the Environment)
##---------------------------------------------------------------------------------------------------------
class Sample:
	def __init__(self, startPoint):
		self.pathFound = False
		self.isAlive = True
		self.isFittest = False
		self.color = (100, 100, 100)
		
		#Kinematics
		self.kinematics = PointMassKinematics(startPoint)
		
		#Genetic Attributes & Decision Making
		self.fitness = 0
		self.genetics = Genetics(1000)

	# Takes the next decision in self.genetics.decisionMakingGenes
	def makeADecision(self, env, numStepsInCurrentOptimumPath):
		if(self.isStillAlive(env)):
			if(len(self.genetics.decisionMakingGenes) > self.genetics.decisionsMade):
				#randomly move in a given direction made by the decision making genetics
				self.kinematics.a = self.genetics.decisionMakingGenes[self.genetics.decisionsMade]
				self.genetics.decisionsMade = self.genetics.decisionsMade + 1
			else:
				self.isAlive = False
			if(self.genetics.decisionsMade > numStepsInCurrentOptimumPath):
				self.isAlive = False
			self.kinematics.accelerate()
	
	# check if sample is still alive based on the environment
	def isStillAlive(self, env):
		for obstacle in env.obstacles:
			obstacleOrigin, obstacleRadius = obstacle
			if(self.kinematics.obstacleHit(obstacleOrigin, obstacleRadius)):
				self.isAlive = False
		if(self.isAlive and self.kinematics.endPointFound(env.endPoint)):
			self.isAlive = False
			self.pathFound = True
		if(self.isAlive and self.kinematics.wallHit(env.screenSizeX, env.screenSizeY)):
			self.isAlive = False
		return self.isAlive

	# Sets the sample as the fittest sample, so it can be placed directly into the next generation
	# thanks to Code-Bullet: https://github.com/Code-Bullet/Smart-Dots-Genetic-Algorithm-Tutorial for the algorithm
	def setAsFittestSample(self, startPoint):
		self.isFittest = True
		self.isAlive = True
		self.kinematics = PointMassKinematics(startPoint)
		self.color = (0, 0, 255)
		self.pathFound = False
		self.genetics.resetDecisions()
	
	# Calculates the fitness for the sample based on either 1) if it found a path 2) how close it was if it didn't
	# thanks to Code-Bullet: https://github.com/Code-Bullet/Smart-Dots-Genetic-Algorithm-Tutorial for the algorithm
	def calculateFitness(self, endPoint):
		if(self.pathFound):
			self.fitness = 1/16 + 10000.0/((self.genetics.decisionsMade)**2)
		else:
			self.fitness = 2.0/((self.kinematics.p.x - endPoint.x)**2 + (self.kinematics.p.y - endPoint.y)**2)
	
	# create a new sample with mutated genetics from the sample
	def procreate(self, startPoint):
		baby = Sample(startPoint);
		baby.genetics = self.genetics.clone()
		return baby;

##---------------------------------------------------------------------------
## Point Mass Kinematics: Models how a Sample interacts with it's Environment
##---------------------------------------------------------------------------
class PointMassKinematics:
	def __init__(self, startPoint):
		self.p = Vector(startPoint.x, startPoint.y)
		self.v = Vector(0, 0)
		self.a = Vector(0, 0)
		
	def obstacleHit(self, obstacleOrigin, obstacleRadius):
		return (self.p.distanceToPoint(obstacleOrigin) < obstacleRadius)

	def wallHit(self, wallX, wallY):
		buffer = 5
		return (self.p.x < buffer or self.p.x > (wallX - buffer) or self.p.y < buffer or self.p.y > (wallY - buffer))
			
	def endPointFound(self, endPoint):
		endPointSize = 15
		return (self.p.distanceToPoint(endPoint) < endPointSize)
	
	def accelerate(self):
		self.v.add(self.a)
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
		self.decisionsMade = 0
		self.decisionMakingGenes = []
		self.randomize(size)

	# randomizes unit vectors for each gene in the genetics
	# thanks to Code-Bullet: https://github.com/Code-Bullet/Smart-Dots-Genetic-Algorithm-Tutorial
	# for the algorithm
	def randomize(self, size):
		for i in range(size):
			f = random.random() * (2*3.14159)
			self.decisionMakingGenes.append(Vector(math.cos(f), math.sin(f)))

	# resets the decisions for the next decision
	def resetDecisions(self):
		self.decisionsMade = 0
	
	# clones the genetics of a sample but with occasional mutations
	# thanks to Code-Bullet: https://github.com/Code-Bullet/Smart-Dots-Genetic-Algorithm-Tutorial
	# for the algorithm
	def clone(self):
		c = Genetics(len(self.decisionMakingGenes))
		c.decisionMakingGenes = []
		mutationRate = 0.01 #unit: % def: chance that any vector in decisionMakingGenes gets changed
		for decision in self.decisionMakingGenes:
			f = random.random()
			if (f < mutationRate):
				f = random.random() * (2*3.14159)
				c.decisionMakingGenes.append(Vector(math.cos(f), math.sin(f)))
			else:
				c.decisionMakingGenes.append(decision)
		return c;