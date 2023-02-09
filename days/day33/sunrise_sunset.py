import requests
import datetime

LAT = -15.826691
LONG = -47.921822

parameters = {
    'lat': LAT, 
    'lng': LONG,
    'formatted': 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data.get('results').get('sunrise').split('T')[1].split(':')[0]
sunset = data.get('results').get('sunset').split('T')[1].split(':')[0]

print(sunrise, sunset)