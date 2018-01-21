import random
from GA import max_power
def mutate(powers):
    """Randomly mutate one part of population.
    Args:
        powers: The power vector to mutate part of
    """
    # Choose a random element
    mutation = random.randrange(0,len(powers)-1)

    # Mutate one of the power elements.
    powers[mutation] = random.randrange(0,max_power);

    return powers
