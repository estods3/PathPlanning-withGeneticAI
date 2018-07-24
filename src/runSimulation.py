import pygame
from Sample import Sample
from Population import Population
from environment import Environment

################
# Main Program #
################

env = Environment(1000, 300)
pop = Population(1000, env)

while(True):
	# check if game was exited
	#-------------------------
	env.checkExited()
	
	#Simulate Population
	#-------------------
	while pop.isNotExtinct():
		env.checkExited()
		pop.moveSamples()
		env.redrawEnv(pop)
	
	#Genetic Algorithm
	#-----------------
	pop.performNaturalSelectionAndReproduction()
	env.clearPath()