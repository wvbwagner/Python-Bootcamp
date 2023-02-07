import pandas
import datetime
import smtplib
from random import choice

email = 'wagner.botelho@gmail.com'
passwd = 'kpgdnzvlngybomvl'
list = []
message = ''


today_tupple = (datetime.datetime.now().month, datetime.datetime.now().day)

data = pandas.read_csv('birthdays.csv')
bdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

for i in range(1,3):
    with open (f'letter_{i}.txt') as file:
        list.append(file.read().strip())

if today_tupple in bdays_dict:
    person = bdays_dict[today_tupple]
    message = choice(list).replace('[NAME]', person['name'])   
    with smtplib.SMTP('smtp.gmail.com', port=587) as conns:
        conns.starttls()
        conns.login(user=email, password=passwd)
        conns.sendmail(from_addr=email, 
        to_addrs='wvbwagner@gmail.com', 
        msg=f"Subject:A message for you\n\n{message}")


