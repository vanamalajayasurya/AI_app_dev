from flask import Flask, render_template, request
import requests

# Tell Flask to look for HTML directly in this folder (not "templates/"),
# and to serve the "css" folder as static files.
app = Flask(__name__, template_folder=".", static_folder="css", static_url_path="/css")

api_key = "609fa5ddb6094bdfb3face2a9c28a02c"


@app.route("/", methods=["GET", "POST"])
def index():
    articles = []
    news_topic = ""
    message = ""

    if request.method == "POST":
        news_topic = request.form.get("topic", "")

        url = f"https://newsapi.org/v2/everything?q={news_topic}&apiKey={api_key}"

        response = requests.get(url)

        data = response.json()

        if data["status"] == "ok":
            for news in data["articles"][:5]:
                articles.append(news)

            if not articles:
                message = "no news"
        else:
            message = "no news"

    return render_template("index.html", articles=articles, topic=news_topic, message=message)


if __name__ == "__main__":
    app.run(debug=True)