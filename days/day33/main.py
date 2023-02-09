import requests
from datetime import datetime
import smtplib
import os
from time import sleep

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
EMAIL = os.environ['EMAIL']
PASSWD = os.environ['EMAIL_PASS']

#Your position is within +5 or -5 degrees of the ISS position.

def is_above_me():
    upper_lat_value = MY_LAT + 5
    lower_lat_value = MY_LAT - 5
    upper_lng_value = MY_LONG + 5
    lower_lng_value = MY_LONG - 5

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    acceptable_latitude = lower_lat_value <= iss_latitude <= upper_lat_value
    acceptable_longitude = lower_lng_value <= iss_longitude <= upper_lng_value

    if acceptable_latitude and acceptable_longitude:
        return True
    return False





#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    return False



while True:
    sleep(180)
    if is_night() and is_above_me():
        with smtplib.SMTP('smtp.gmail.com', port=587) as conns:
            conns.starttls()
            conns.login(user=EMAIL, password=PASSWD)
            conns.sendmail(from_addr=EMAIL,
            to_addrs='wvbwagner@gmail.com',
            msg=f"Subject:There goes ISS\n\n{'Look to the sky NOW!'}")       
