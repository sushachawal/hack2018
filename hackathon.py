import GA
import evolve
from API_functions import getCourseInfo
import matplotlib.pyplot as plt

x = getCourseInfo()["x"]
y = getCourseInfo()["y"]
datalength = len(x)
length = 7;
section_power = [400] * length

print "Constant 400W gives {} ".format(evolve.simulation.get_time(section_power))


#print "Initial population of {} gives {}".format(len(population), evolve.simulation.get_time(population[0]))

hugepop = []

for popnumber in range(25):
    population = GA.create_population(30)
    for i in range(50):
        newpop = evolve.evolve(population)
        population = newpop
        #print "Population of {} members gives latest value of = {} ".format(len(newpop), evolve.simulation.get_time(newpop[0]))
    hugepop.append(population[0])
    print "Population of {} members gives latest value of = {} ".format(len(newpop), evolve.simulation.get_time(newpop[0]))
for i in range(50):
    finalpop = evolve.evolve(hugepop)
    hugepop = finalpop
print "Hugepop generated best time of {}".format(evolve.simulation.get_time(hugepop[0]))

plotpower = []
for i in range(datalength):
    for j in range(0, len(evolve.simulation.section_dist)):
        if x[i] <= evolve.simulation.section_dist[j]:
            plotpower.append(hugepop[0][j])
            break

#print plotpower
plt.figure(1)
plt.subplot(211)
plt.plot(x,plotpower,'-r')
plt.subplot(212)
plt.plot(x,y,'-r')
plt.figure(1).show()
plt.figure(1).savefig('HugePopPowerPlotandElev' + '.pdf', bbox_inches='tight')

# if stream in streams.keys():
#     print(stream)

# print athlete_data.email
