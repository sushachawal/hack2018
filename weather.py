import requests

URL = "http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&APPID=c5914720e06793445e324ce52bab4f8c"

data = requests.get(URL).json()

print data["wind"]
