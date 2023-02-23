import requests
import os
from datetime import datetime
from requests.auth import HTTPBasicAuth

USER  = os.environ['EMAIL']
PASS = os.environ['SHEETY']
API_KEY = '21e82053c5c8c23845d51622e21ffc79'
APP_ID = '3ca599a9'

GENDER = 'male'
WEIGHT_KG = 75.5
HEIGHT_CM = 171
AGE = 40

workout_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = 'https://api.sheety.co/6688bdd6bb80a9aa19fbb96bf05b325c/workouts/workouts'

text = input('Which exercises you did: ')

parameters = {
    'query': text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE, 
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

response = requests.post(workout_endpoint, json=parameters, headers=headers)
answer = response.json()

date = datetime.now().date().strftime('%d/%m/%Y')
time = datetime.now().strftime('%X')

for exercise in answer.get('exercises'):
    params_test = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise.get('name').title(),
            'duration': exercise.get('duration_min'),
            'calories': exercise.get('nf_calories')
        }
    }
    spread = requests.post(sheety_endpoint, json=params_test, headers={"Authorization": PASS})
    print(spread.text)
