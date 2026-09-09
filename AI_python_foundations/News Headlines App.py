import requests

api_key = "609fa5ddb6094bdfb3face2a9c28a02c"

news_topic = input("Enter News Topic: ")



url = f"https://newsapi.org/v2/everything?q={news_topic}&apiKey={api_key}"


response = requests.get(url)

data = response.json()

if data["status"] == "ok" :
    print(f"\n📰 Top News for {news_topic}\n")

    for news in data ["articles"][:5]:
        print("•", news["title"])

    else:
        print("no news")

