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

print streams.keys()

# if stream in streams.keys():
#     print(stream)

# print athlete_data.email