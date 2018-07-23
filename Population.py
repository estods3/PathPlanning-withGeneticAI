import pygame
from Sample import Sample, Vector
from environment import Environment
import random

class Population:
	def __init__(self, size, env):
		self.popSize = size
		self.env = env
		self.generation = 1
		self.fitnessSum = 0
		self.minStep = 1000
		self.samples = []
		for i in range(0, self.popSize):
			self.samples.append(Sample(self.env.startX, self.env.startY, self.env.endX, self.env.endY))
		
	def performNaturalSelectionAndReproduction(self):
		newSamples = []
		#todo setBestSample() (optimizedPath())
		fitnessSum = 0
		bestFitness = -1
		bestSample = []
		for sample in self.samples:
			sample.calculateFitness()
			if(sample.fitness > bestFitness):
				bestFitness = sample.fitness
				bestSample = sample
			fitnessSum = fitnessSum + sample.fitness
		for sample in self.samples:
			parent = self.selectParent(fitnessSum)
			baby = parent.procreate()
			#baby.genetics.mutate()
			newSamples.append(baby)
		newSamples[0] = sample
		self.samples = newSamples
		self.generation = self.generation + 1
			
	def selectParent(self, fitnessSum):
		if(fitnessSum <= 0):
			i = 0
		else:
			i = random.random() * (fitnessSum)
		runningSum = 0
		for sample in self.samples:
			runningSum = runningSum + sample.fitness
			if(runningSum > i):
				return sample
		
	def isNotExtinct(self):
		if(self.samples == []):
			return True
		for sample in self.samples:
			for obstacle in self.env.obstacles:
				obstacleOrigin, obstacleRadius = obstacle
				sample.kinematics.obstacleHit(obstacleOrigin, obstacleRadius)
			sample.kinematics.endPointFound(Vector(self.env.endX, self.env.endY))
			sample.kinematics.wallHit(self.env.screenSizeX, self.env.screenSizeY)
			if(sample.kinematics.isAlive):
				return True		
		return False