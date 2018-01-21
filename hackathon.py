import GA
import evolve

section_power = [400,400,400,400,400,400,400]

print "Constant 400W gives {} ".format(evolve.simulation.get_time(section_power))

population = GA.create_population(10)

print "Initial population gives {}".format(evolve.simulation.get_time(population[0]))

for i in range(10):
    newpop = evolve.evolve(population)
    population = newpop
    print "Latest value = {} ".format(evolve.simulation.get_time(newpop[0]))

# if stream in streams.keys():
#     print(stream)

# print athlete_data.email
