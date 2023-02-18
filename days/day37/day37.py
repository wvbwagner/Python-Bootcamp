import requests
from datetime import datetime, timedelta

USERNAME = 'wbotelho'
TOKEN = 'PythonDay37'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': "Graph Name",
    'unit': 'Km',
    'type': 'float',
    'color': 'sora',
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)
today = datetime.now().date()
string_data = today.strftime("%Y%m%d")

posting_endpoint = f"{graph_endpoint}/{graph_config.get('id')}"

graph_info = {
    'date': string_data,
    'quantity': '5.5', 
}

#response = requests.post(url=posting_endpoint, json=graph_info, headers=headers)
#print(response.text)

updating_endpoint = f'{posting_endpoint}/{string_data}'

graph_update = {
    'quantity': '118.5'
}

#response = requests.put(url=updating_endpoint, json=graph_update, headers=headers)
#print(response.text)

delete_endpoint = f'{posting_endpoint}/20230215'

response = requests.delete(url=delete_endpoint, json=graph_update, headers=headers)
print(response.text)