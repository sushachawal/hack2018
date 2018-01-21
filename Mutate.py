import random
from GA import max_power, min_power
def mutate(powers):
	"""Randomly mutate one part of population.
	Args:
		powers: The power vector to mutate part of
	"""
	# Choose a random element
	mutation_chance = 0.1
	mutation = random.randrange(0,len(powers))

	# Mutate one of the power elements.
	i = 0
	for i in range(0, len(powers)):
		if (mutation_chance  > random.random()) and i <3:
			powers[i] = random.randrange(min_power,max_power);
			i +=1
		else:
			break

	return powers
