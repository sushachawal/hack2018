# import numpy as np
import random
import numpy as np
from leastsquares import leastsquares
from evolve import evolve

def create_test_data(m,c,var):
    y = []
    for x in range(0,100):
        y.append(m*(x/10) + c + (random.randrange(-var*10,var*10)/100))
    return y

def create_population(size):

    pop = []
    for i in range(0, size):
        line = {"m":random.randint(0,10), "c": random.randint(0,10)}
        pop.append(line)
    return pop

population = create_population(5)
print population
data = create_test_data(3, -6 , 1)

max_power = 500
min_power = 0
percentage_good = 25

evolve(population, data)

print population

"""
graded = [(score(member), member) for member in population]

graded = [x[1] for x in sorted(graded, key=lambda x:x[0], reverse = True)]

print population
print graded
"""
