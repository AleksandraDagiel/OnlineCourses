import requests
import datetime
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_STOCK = "SOT4E0X3TD8GL028"
API_KEY_NEWS = "1c71cc983bac40e99ee40da812efe49b"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_STOCK,
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

#My idea
# yesterday_date = ((str(datetime.datetime.today() - datetime.timedelta(days=1))).split(" "))[0]
# yesterday_closing_price = float(stock_data[yesterday_date]['4. close'])
# day_before_yesterday_date = ((str(datetime.datetime.today() - datetime.timedelta(days=2))).split(" "))[0]
# day_before_yesterday_closing_price = float(stock_data[day_before_yesterday_date]['4. close'])
# difference = abs(day_before_yesterday_closing_price - yesterday_closing_price)
# percentage_diff = (difference/yesterday_closing_price) * 100
# parameters = {
#     "q": COMPANY_NAME,
#     "from": yesterday_date,
#     "sortBy": "publishedAt",
#     "apiKey": API_KEY_NEWS,
# }

# if percentage_diff > 5:
#     response = requests.get(url=NEWS_ENDPOINT, params=parameters)
#     response.raise_for_status()
#     news_data = response.json()["articles"]
#     last_news = []
#     [last_news.append(news) for news in news_data]
#     recent_news = last_news[:3]
#
#     api_key = os.environ.get("OWM_API_KEY")
#     account_sid = os.environ.get("OWM_ACC_SID")
#     auth_token = os.environ.get("OWM_AUTH_TOKEN")
#
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body=f"{STOCK_NAME}: {percentage_diff}%\n"
#              f"Headline: {recent_news[0]['source']['title']}\n"
#              f"Brief: {recent_news[0]['source']['description']}",
#         from_='+12073604858',
#         to='+48884617302',
#     )

#Course idea
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": API_KEY_NEWS,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\n Headline: {article['title']} \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    api_key = os.environ.get("OWM_API_KEY")
    account_sid = os.environ.get("OWM_ACC_SID")
    auth_token = os.environ.get("OWM_AUTH_TOKEN")

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12073604858',
            to='+48884617302',
        )