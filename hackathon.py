import GA
import evolve
from API_functions import getCourseInfo

length = len(getCourseInfo()["x"])
section_power = [400] * length

print "Constant 400W gives {} ".format(evolve.simulation.get_time(section_power))

population = GA.create_population(30)

print "Initial population of {} gives {}".format(len(population), evolve.simulation.get_time(population[0]))

for i in range(40):
    newpop = evolve.evolve(population)
    population = newpop
    print "Population of {} members gives latest value of = {} ".format(len(newpop), evolve.simulation.get_time(newpop[0]))
print population
# if stream in streams.keys():
#     print(stream)

# print athlete_data.email
