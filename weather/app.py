from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder=".", static_url_path="")

API_KEY = "b8ba3ef16bce06722887202ec0df69a5"


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"message": "city is required"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        wind = data["wind"]["speed"]

        return jsonify({
            "city": city_name,
            "country": country,
            "temp": temp,
            "humidity": humidity,
            "condition": condition,
            "description": description,
            "icon": icon,
            "wind": wind,
        }), 200
    else:
        return jsonify({"message": data.get("message", "error")}), response.status_code


if __name__ == "__main__":
    app.run(debug=True, port=5000)