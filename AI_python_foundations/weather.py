import requests

API_KEY = "c421d43b44c22e1669629bba075bcc85"

print("🌦️ Weather App")
print("-" * 30)

city = input("Enter city name: ")

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
    wind = data["wind"]["speed"]

    print("\n📍 Weather Report")
    print(f"City        : {city_name}, {country}")
    print(f"🌡️ Temperature : {temp}°C")
    print(f"☁️ Condition   : {condition}")
    print(f"📝 Description : {description}")
    print(f"💧 Humidity    : {humidity}%")
    print(f"💨 Wind Speed  : {wind} m/s")
else:
    print("❌ Error:", data["message"])