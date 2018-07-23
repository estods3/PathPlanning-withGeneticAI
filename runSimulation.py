import pygame
from Sample import Sample
from Population import Population
from environment import Environment

################
# Main Program #
################

#todo, have environment generate random obstacles or varying shape. have shape have collision impact

env = Environment(1000, 300)
pop = Population(1000, env)

while(True):
	# check if game was exited
	#-------------------------
	env.checkExited()
	
	#Simulate Population
	#-------------------
	print("Generation: " + str(pop.generation))
	while pop.isNotExtinct():
		env.checkExited()
		for sample in pop.samples:
			sample.move()
		env.redrawEnv(pop)
	pygame.display.update()
	
	#Genetic Algorithm
	#-----------------
	pop.performNaturalSelectionAndReproduction()