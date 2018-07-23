import pygame
from Sample import Sample, Vector, PointMassKinematics
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
		fitnessSum = 0
		bestFitness = -1
		bestSample = []
		for sample in self.samples:
			sample.calculateFitness()
			if(sample.fitness > bestFitness):
				bestFitness = sample.fitness
				bestSample = sample
				self.minStep = sample.genetics.step
			fitnessSum = fitnessSum + sample.fitness
		for sample in self.samples:
			parent = self.selectParent(fitnessSum)
			baby = parent.procreate()
			newSamples.append(baby)
		
		bestSample.kinematics = PointMassKinematics(self.env.startX, self.env.startY)
		bestSample.color = (0, 255, 255)
		bestSample.pathFound = False
		bestSample.genetics.step = 0
		newSamples[0] = bestSample
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
			if(sample.isStillAlive(self.env)):
				return True		
		return False