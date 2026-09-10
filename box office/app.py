# ===== Movie Finder App =====
from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder=".", static_url_path="")

api_key = "ae4d0197"


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/api/movie")
def get_movie():
    movie_name = request.args.get("title", "")

    url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie_name}"

    response = requests.get(url)
    data = response.json()

    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        return jsonify({
            "Response": "True",
            "Title": data["Title"],
            "Year": data["Year"],
            "imdbRating": data["imdbRating"],
            "Poster": data.get("Poster", "N/A"),
        })
    else:
        return jsonify({"Response": "False"})


if __name__ == "__main__":
    app.run(debug=True)