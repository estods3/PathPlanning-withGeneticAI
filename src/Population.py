import pygame
from Sample import Sample, Vector, PointMassKinematics
from environment import Environment
import random

##----------------------------------------------------------------------------------
## Population: generates random samples, performs natural selection and reproduction
## for all proceeding generations
##----------------------------------------------------------------------------------
class Population:
	def __init__(self, size, env):
		self.popSize = size
		self.env = env
		self.numStepsInCurrentOptimumPath = 1000
		
		# Create Generation 1 Samples
		self.samples = []
		self.generation = 1
		for i in range(0, self.popSize):
			self.samples.append(Sample(self.env.startPoint))
	
	# each sample makes the next decision
	def moveSamples(self):
		for sample in self.samples:
			sample.makeADecision(self.env, self.numStepsInCurrentOptimumPath)
	
	# randomly (naturally) choses parents for the next generation of samples
	# the samples are clones from their parents, but will the occasional mutation
	def performNaturalSelectionAndReproduction(self):
		nextGeneration = []
		populationFitnessSum = 0
		fittestSample_fitness = -1
		fittestSample = []
		for sample in self.samples:
			sample.calculateFitness(self.env.endPoint)
			if(sample.fitness > fittestSample_fitness):
				fittestSample_fitness = sample.fitness
				fittestSample = sample
				self.numStepsInCurrentOptimumPath = sample.genetics.decisionsMade
			populationFitnessSum = populationFitnessSum + sample.fitness
		for sample in self.samples:
			parent = self.selectParent(populationFitnessSum)
			baby = parent.procreate(self.env.startPoint)
			nextGeneration.append(baby)
		
		fittestSample.setAsFittestSample(self.env.startPoint)
		nextGeneration[0] = fittestSample
		self.samples = nextGeneration
		self.generation = self.generation + 1
	
	# Returns a random sample based on the fitnesses of each sample in the population
	# samples that have a higher fitness are more likely to be chosen as parents
	# thanks to Code-Bullet: https://github.com/Code-Bullet/Smart-Dots-Genetic-Algorithm-Tutorial
	# for the algorithm
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
	
	# determines if the population is still running a simulation (True)
	def isNotExtinct(self):
		if(self.samples == []):
			return True
		for sample in self.samples:
			if(sample.isStillAlive(self.env)):
				return True		
		return False