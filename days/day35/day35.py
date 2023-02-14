import requests
import datetime
import smtplib
import os

email = os.environ['EMAIL']
passwd = os.environ['EMAIL_PASS']

api_key = os.environ['OPENWEATHER']

today = str(datetime.datetime.now().date())

parameters = {
    'lat': -15.826691,
    'lon': -47.921822,
    'appid': api_key
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameters)
data = response.json()
weather_condition_list = data.get('list')
size = len(weather_condition_list)
time_of_rain = []
for i in range(size):
    if int(weather_condition_list[i].get('weather')[0].get('id')) < 600:
        alerts = (weather_condition_list[i].get('dt_txt').split())
        if today in alerts:
            time_of_rain.append(alerts[1])

message = 'It is going to rain at'

if len(time_of_rain) > 0:
    for hours in time_of_rain:
        message += (f' {hours}, ')
else:
    message = 'No rain forecasted for today'   

with smtplib.SMTP('smtp.gmail.com', port=587) as conns:
    conns.starttls()
    conns.login(user=email, password=passwd)
    conns.sendmail(from_addr=email, to_addrs='wvbwagner@gmail.com',
    msg=f'Subject:Watch for rain\n\n{message}')
