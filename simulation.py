import math
import numpy as np
from API_functions import getCourseInfo
from API_functions import getWindInfo


courseData = getCourseInfo()
x = courseData['x']
y = courseData['y']
inclin = courseData['inclin']
latlng = courseData['latlng']

wind = getWindInfo(latlng[0][0],latlng[0][1])

section_dist = [1866.5, 3634.7, 5691.2, 7926.5, 9665.1, 11521.7, 14032.9]

def get_time(section_power):
	energy = 3000*1000
	velocities = []
	mass = 90
	g = 9.81

	area = 0.32
	Cd = 0.88
	A = 0.5 * 1.225 * area * Cd

	Fr = 0.004

	D = 0.5 * mass
	time = 0
	windAngle = 270 - wind['deg'] #Converts meteorological angle to standard angle measurement system
	for i in range(len(x)-1):
		if i == 0:
			v_prev = 0
		else:
			v_prev = velocities[i - 1]
			
		deltaLat = latlng[i + 1][0] - latlng[i][0]
		deltaLng = latlng[i + 1][1] - latlng[i][1]
		heading = math.atan2(deltaLat,deltaLng)
		wind_v = -1 * wind["speed"] * math.cos(heading - windAngle) # 1 if fully opposing motion, -1 if in same direction

		distance = math.sqrt((x[i + 1] - x[i])**2 + (y[i + 1] - y[i])**2)
		
		theta = math.atan(inclin[i]/100)
		B = Fr * mass * g * math.cos(theta)
		C = mass * g * math.sin(theta)
		E = D / distance;
		#P = section_power[i]
		for j in range(0, len(section_dist)):
			if x[i] < section_dist[j]:
				P = section_power[j]
				break

		coeff = [A + E, 2* A * wind_v, B + C + A * wind_v * wind_v - E * v_prev*v_prev, -P]
		#coeff = [A, 2 * wind_v * A, B + C + A * wind_v * wind_v, - P]
		#coeff = [A,0,B+C,-P]
		v_array = np.roots(coeff)

		tempV = 0;
		for n in v_array:
			if n.imag == 0 and n.real > tempV.real:
				tempV = n
		if tempV.real <= 0:
			print "WARNING: Non-Positive velocities"
			print "Section failure: {}".format(section_power[i])
			print "Index of failure: {}".format(i)
			print tempV.real
			time += 1000000000
			return time.real
		if P == 0:
			print velocities[i]
		velocities.append(tempV.real)	

		delta_time = distance/velocities[i]
		time += delta_time

		energy -= P * delta_time

		# if i == 0:
			# prev_velocity = 0
		# else:
			# prev_velocity = velocities[i -1]

		# delta_KE = D * (velocities[i]**2 - prev_velocity**2)
		# if delta_KE > 0:
			# energy -= delta_KE

		if energy < 0:
			time += 100000000
			return time.real
	return time.real
	#return {"time": time.real, "velocities": velocities}
