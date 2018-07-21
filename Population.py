import pygame
from Sample import Sample
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
		
	def calculateFitnesses(self):	
		for sample in self.samples:
			sample.calculateFitness()
	
	def performNaturalSelection(self):
		newSamples = []
		self.calculateFitnesses()
		#todo setBestSample() (optimizedPath())
		fitnessSum = 0
		for sample in self.samples:
			fitnessSum = fitnessSum + sample.fitness
		#todo put best dot as first element of newSamples
		for sample in self.samples:
			parent = self.selectParent(fitnessSum)
			baby = parent.procreate()
			baby.genetics.mutate()
			newSamples.append(baby)

		samples = newSamples
		self.generation = self.generation + 1
			
	def selectParent(self, fitnessSum):
		if(fitnessSum <= 0):
			i = 0
		else:
			i = random.randint(0, int(fitnessSum))
		runningSum = 0
		for sample in self.samples:
			runningSum = runningSum + sample.fitness
			if(runningSum > i):
				return sample
		
	def isNotExtinct(self):
		if(self.samples == []):
			return True
		for sample in self.samples:
			sample.obsticleOrWallHit(self.env)
			sample.endPointFound(self.env)
			if(sample.isAlive):
				return True		
		return False