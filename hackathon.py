import csv
import GA
import evolve
from API_functions import getCourseInfo
import matplotlib.pyplot as plt

x = getCourseInfo()["x"]
y = getCourseInfo()["y"]
datalength = len(x)
length = 7
section_power = [400] * length

constantP = evolve.simulation.get_time(section_power)

print "Constant 400W gives {} ".format(constantP["time"])

velocities = constantP["velocities"]

with open("test.csv", "wb") as csvfile:
    f=csv.writer(csvfile)
    f.writerow(x)
    f.writerow(y)
    f.writerow([velocity.real for velocity in velocities])

#print "Initial population of {} gives {}".format(len(population), evolve.simulation.get_time(population[0]))

hugepop = []

for popnumber in range(5):
    population = GA.create_population(5)
    for i in range(5):
        newpop = evolve.evolve(population)
        population = newpop
        #print "Population of {} members gives latest value of = {} ".format(len(newpop), evolve.simulation.get_time(newpop[0]))
    hugepop.append(population[0])
    print "Population of {} members gives latest value of = {} ".format(len(newpop), evolve.simulation.get_time(newpop[0])["time"])
for i in range(5):
    finalpop = evolve.evolve(hugepop)
    hugepop = finalpop

bestpower = evolve.simulation.get_time(hugepop[0])
velocities = bestpower["velocities"]
print "Hugepop generated best time of {}".format(bestpower["time"])
with open("test2.csv", "wb") as csvfile:
    f=csv.writer(csvfile)
    f.writerow(x)
    f.writerow(y)
    f.writerow([velocity.real for velocity in velocities])

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
