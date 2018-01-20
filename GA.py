# import numpy as np
import random


max_power = 500
min_power = 0

def create_population(size):

    pop = []

    for i in range(0, size):
        powers = []
        for i in range(0,7):
            powers.append(random.randint(min_power, max_power))

        pop.append(powers)

    return pop




def calculate_time(powers):


