import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()#lança uma exceção caso response code não seja 200
teste = response.json()

latitude = teste.get('iss_position').get('latitude')
longitude = teste.get('iss_position').get('longitude')

iss_pos = (latitude, longitude)