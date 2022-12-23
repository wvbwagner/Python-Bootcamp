
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    global travel_log
    newDict = {}
    newDict['country'] = country
    newDict['visits'] = visits
    newDict['cities'] = cities
    travel_log.append(newDict)

'''def whichCities():
    cities = []
    while True:
        places = input("Enter the cities you've visited (or stop to finish): ")
        if places == 'stop':
            break
        else:
            cities.append(places)
    return cities'''
add_new_country('Russia', 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
