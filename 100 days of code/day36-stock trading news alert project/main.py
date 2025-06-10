import requests
from twilio.rest import Client

# Constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = 
NEWS_API_KEY =
TWILIO_SID =
TWILIO_AUTH_TOKEN =

# Step 1: Get stock data
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_close = float(data_list[0]["4. close"])
day_before_close = float(data_list[1]["4. close"])

# Step 2: Calculate difference and percentage
price_diff = yesterday_close - day_before_close
up_down = "🔺" if price_diff > 0 else "🔻"
percent_diff = abs(price_diff) / day_before_close * 100

# Step 3: If change > 5%, fetch news
if percent_diff > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"][:3]  # First 3 articles

    # Step 4: Format messages
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{round(percent_diff)}%\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description']}"
        for article in articles
    ]

    # Step 5: Send via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+19786254472",  # Your Twilio number
            to="+919947613366"     # Your phone number
        )
        print(f"Sent: {message.sid}")
else:
    print("Stock change is not significant.")
