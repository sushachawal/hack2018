import math
import numpy

velocities = []
y = []
x = []
inclin = []

mass = 90
g = 9.81

area = 0.32
Cd = 0.88
A = 0.5 * 1.225 * area * Cd

Fr = 0.004
B = Fr * mass * g

D = 0.5 * mass

time = 0

energy = 1000
#define energy properly


def get_time(x, y, inclin, section_dist, section_power):
    time = 0
    for i in range(0, x.len() - 1):
        theta = math.arctan(inclin[i]/100)
        C = mass * g * math.sin(theta)

        for j in range(0, section_dist.len()):
            if x[i] < section_dist[j]:
                P = section_power[j]
                break


        coeff = [A, O, B + C, - P]
        v_array = np.roots(coeff)

        for n in v_array:
            if n.imag == 0:
                velocities[i] = n
                break

        distance = math.sqrt((x[i + 1] - x[i])**2 + (y[i + 1] - y[i])**2)

        delta_time = distance/velocities[i]
        time += delta_time

        energy -= P * delta_time

        if i == 0:
            prev_velocity = 0
        else:
            prev_velocity = velocities[i -1]

        energy -= D * (velocities[i]**2 - prev_velocity**2)

        if energy < 0:
            time += 1000000000
            break
        return time
