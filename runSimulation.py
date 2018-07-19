
from Sample import Sample
from Population import Population
from environment import Environment

#Main Program

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
	print(p.generation)
	#genetic algorithm
	#-----------------
	#p.calculateFitnesses();
    #p.performNaturalSelection();
    #p.populate();