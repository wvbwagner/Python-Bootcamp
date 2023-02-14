import requests
from datetime import datetime, timedelta
import smtplib
import os

EMAIL = os.environ['EMAIL']
PASSWD = os.environ['EMAIL_PASS']

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_PARAMETERS = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
    'apikey': 'YCRO0AMF5E7B31FC',
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_PARAMETERS = {
    'apiKey': '0e731e51e66447a1b8a6759a9fbe7b6e',
    'qInTitle': COMPANY_NAME,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETERS)
response.raise_for_status()
data = response.json()
data_list = [value for (key, value) in data.get('Time Series (Daily)').items()]
yesterday_closing_price = float(data_list[0].get('4. close'))

#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_closing_price = float(data_list[1].get('4. close'))

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(yesterday_closing_price - before_yesterday_closing_price)
message = 'TSLA DOWN'
if yesterday_closing_price > before_yesterday_closing_price:
    message = 'TSLA UP'

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage = difference / yesterday_closing_price * 100

#TODO 5 and 6. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage > 0.5:
    resp = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    resp.raise_for_status()
    news = resp.json().get('articles')
    
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
top_three = news[:3] 


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 7. - Create a new list of the first 3 article's headline and description using list comprehension.
news_list = [f"HeadLine: {article.get('title')}. \nBrief: {article.get('description')}" for article in top_three]

#TODO 8. - Send each article as a separate message via Twilio. 
for article in news_list:
    with smtplib.SMTP('smtp.gmail.com', port=587) as conns:
        conns.starttls()
        conns.login(user=EMAIL, password=PASSWD)
        conns.sendmail(from_addr=EMAIL, to_addrs='wvbwagner@gmail.com', msg=f"Subject:{message} {percentage:.2f} \n\n{article}")
        

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

