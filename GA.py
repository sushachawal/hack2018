# import numpy as np
import random
import numpy as np

max_power = 500
min_power = 0
percentage_good = 25

def score(x):
    return max(x)

def create_population(size):

    pop = []

    for i in range(0, size):
        powers = []
        for j in range(0,7):
            powers.append(random.randint(min_power, max_power))

        pop.append(powers)


    return pop

population = create_population(5)

graded = [(score(member), member) for member in population]

graded = [x[1] for x in sorted(graded, key=lambda x:x[0], reverse = True)]

print population
print graded
