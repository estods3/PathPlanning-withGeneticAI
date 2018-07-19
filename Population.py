import pygame
from Sample import Sample
from environment import Environment

class Population:
	def __init__(self, size, env):
		self.popSize = size
		self.env = env
		self.generation = 1
		
		self.samples = []
		for i in range(0, self.popSize):
			self.samples.append(Sample(self.env.startX, self.env.startY, self.env.endX, self.env.endY))
		
	#def calculateFitnesses():	
	
	#def performNaturalSelection():
		
	
	#def selectParent():
		
		
	#def endPointReached():
		
		
	#def populate():
	#	this.generation = this.generation + 1
		
	def isNotExtinct(self):
		for sample in self.samples:
			sample.obsticleOrWallHit(self.env)
			if(sample.isAlive):
				return True		
		return False