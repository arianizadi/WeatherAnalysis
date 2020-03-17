import requests
import json
import matplotlib.pyplot as plt
from geopy import Nominatim
from GLOBAL_VARIBLES import API_KEY, LOCATION


# GETTING LOCATION INFORMATION

geolocator = Nominatim(user_agent="WeatherAnalysis")

location = LOCATION

location = geolocator.geocode(location, addressdetails=True)

print('\n\nLocation Info: ' + str(location.address))
print('Lat: ' + str(location.latitude))
print('Long: ' + str(location.longitude) + '\n\n')


# GETTING WEATHER INFORMATION

url = 'https://api.darksky.net/forecast/' + API_KEY + \
    '/' + str(location.latitude) + ',' + str(location.longitude)

r = requests.get(url)


# PROCESSING WEATHER INFORMATION

yLabels = []
xLabels = []

yAxis = 'temperatureMax'
xAxis = 'daily'

count = 0

for day in r.json()[xAxis]['data']:
    xLabels.append(count)
    yLabels.append(day[yAxis])
    # POINT ANNOTATIONS ON PLT
    plt.annotate(day[yAxis], (count, day[yAxis]))
    count += 1


# CREATE DICT

KEYS = xLabels
VALUES = yLabels

# ZIP INTO DICT

POINT_DICT = dict(zip(KEYS, VALUES))

# SORT DICT

POINT_DICT = sorted(POINT_DICT.items(), key=lambda x: x[1])


# PLOTTING PLT

plt.plot(xLabels, yLabels)
plt.ylabel(yAxis)
plt.xlabel(xAxis)
plt.title(location.raw['address']['city'])
plt.show()

print('\n\n')
