import requests
import stravalib
from stravalib import Client
def getCourseInfo():
	STORED_ACCESS_TOKEN = "903910abaf69b186957a22c1227d6f19237cd233"

	client = Client(access_token=STORED_ACCESS_TOKEN)
	athlete_data = client.get_athlete()
	activity_id = 887327831
	activity = client.get_activity(887327831)

	types = ['time', 'altitude', 'velocity_smooth', 'distance', 'grade_smooth', 'watts','latlng']
	streams = client.get_activity_streams(activity_id, types = types, resolution='medium')

	# for i in range(0, len(streams['time'].data)):
	#     print "{} {}".format(streams['distance'].data[i], streams['watts'].data[i])

	x = streams['distance'].data
	y = streams['altitude'].data
	inclin = streams['grade_smooth'].data
	latlng = streams['latlng'].data
	
	return {'x':x,'y': y, 'inclin':inclin, 'latlng': latlng}
def getWindInfo(lat,lng):
	URL = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon="+ str(lng) + "&APPID=c5914720e06793445e324ce52bab4f8c"
	data = requests.get(URL).json()
	return data["wind"]
