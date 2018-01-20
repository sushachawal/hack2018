def breed(self, mother, father):
    """Make two children as parts of their parents.
    Args:
        mother: power vector of mother
        father: power vector of father
    """
    children = []
    for _ in range(2):

        child = []

        # Loop through the parameters and pick params for the kid.
        for i in range(0,len(mother)-1)
            child[i] = random.choice(
                [mother[i], father[i]]
            )
        children.append(child)
    return children
