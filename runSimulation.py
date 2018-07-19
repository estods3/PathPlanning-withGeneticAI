import pygame
from Sample import Sample
from Population import Population
from environment import Environment

#Main Program
#todo, have environment generate random obstacles or varying shape. have shape have collision impact


e = Environment(640, 480)
p = Population(1000, e)

while(True):
	# check if game was exited
	#-------------------------
	e.checkExited()
	
	#simulate population
	#-------------------
	while p.isNotExtinct():
		e.checkExited()
		for sample in p.samples:
			sample.moveSample()
		e.redrawEnv(p)
	#e.redrawEnv(p)
	
	pygame.display.update()
	print(p.generation)
	
	#genetic algorithm
	#-----------------
	p.calculateFitnesses()
	p.performNaturalSelection()