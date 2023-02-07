import smtplib
import datetime
from random import choice

email = 'wagner.botelho@gmail.com'
passwd = 'kpgdnzvlngybomvl'
now = datetime.datetime.now().weekday()

   
with smtplib.SMTP('smtp.gmail.com', port=587) as conns:
    conns.starttls()
    conns.login(user=email, password=passwd)
    conns.sendmail(from_addr=email, 
    to_addrs='marcpcruz@gmail.com', 
    msg='Subject:A message for you\n\nVá a merda')
