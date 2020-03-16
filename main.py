import requests
import json
import matplotlib.pyplot as plt
from geopy import Nominatim
from GLOBAL_VARIBLES import API_KEY


# GETTING LOCATION INFORMATION

geolocator = Nominatim(user_agent="WeatherAnalysis")

location = ''

while location == '':
    location = input('Location: ')

location = geolocator.geocode(location)

print('\n\nLocation Info: ' + str(location.address))
print('Lat: ' + str(location.latitude))
print('Long: ' + str(location.longitude) + '\n\n')


# GETTING WEATHER INFORMATION

url = 'https://api.darksky.net/forecast/' + API_KEY + \
    '/' + str(location.latitude) + ',' + str(location.longitude)

r = requests.get(url)


# PROCESSING WEATHER INFORMATION

xLabels = []
yLabels = []

aimFor = 'temperatureMax'

count = 0

for day in r.json()['daily']['data']:
    xLabels.append(count)
    yLabels.append(day[aimFor])
    # creating point annotations for plt
    plt.annotate(day[aimFor], (count, day[aimFor]))
    count += 1


# PLOTTING GRAPH


plt.plot(xLabels, yLabels)
plt.ylabel(aimFor)
plt.xlabel('Day')
plt.show()

print('\n\n')
