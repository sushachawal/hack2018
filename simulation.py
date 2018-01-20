import math
import numpy as np
import stravalib
from stravalib import Client

STORED_ACCESS_TOKEN = "903910abaf69b186957a22c1227d6f19237cd233"

client = Client(access_token=STORED_ACCESS_TOKEN)
athlete_data = client.get_athlete()
activity_id = 887327831
activity = client.get_activity(887327831)

types = ['time', 'altitude', 'velocity_smooth', 'distance', 'grade_smooth', 'watts']
streams = client.get_activity_streams(activity_id, types = types, resolution='medium')

# for i in range(0, len(streams['time'].data)):
#     print "{} {}".format(streams['distance'].data[i], streams['watts'].data[i])

x = streams['distance'].data
y = streams['altitude'].data
inclin = streams['grade_smooth'].data
section_dist = [1866.5, 3634.7, 5691.2, 7926.5, 9665.1, 11521.7, 14032.9]

def get_time(section_power):
    energy = 500000
    velocities = []
    mass = 90
    g = 9.81

    area = 0.32
    Cd = 0.88
    A = 0.5 * 1.225 * area * Cd

    Fr = 0.004
    B = Fr * mass * g

    D = 0.5 * mass
    time = 0
    for i in range(len(x)-1):
        theta = math.atan(inclin[i]/100)
        C = mass * g * math.sin(theta)

        for j in range(0, len(section_dist)):
            if x[i] < section_dist[j]:
                P = section_power[j]
                break


        coeff = [A, 0, B + C, - P]
        v_array = np.roots(coeff)

        for n in v_array:
            if n.imag == 0:
                velocities.append(n)
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
    return time.real
