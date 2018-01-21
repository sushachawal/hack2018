# import numpy as np
import random
import numpy as np
from API_functions import getCourseInfo

max_power = 800
min_power = 1

def create_population(size):

	pop = []
	courseData = getCourseInfo()
	length = len(courseData["x"])

	for i in range(0, size):
		powers = []
		
		for j in range(0,length):
			powers.append(random.randint(min_power, max_power))

		pop.append(powers)


	return pop
