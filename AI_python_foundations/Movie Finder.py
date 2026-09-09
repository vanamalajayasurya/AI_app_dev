# ===== Movie Finder App =====
import requests


api_key = "ae4d0197"

movie_name = input("enter the movie name:")

url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie_name}"

response = requests.get(url)
data = response.json()

if data["Response"] == "True":
    print("\n🎬 Movie Details")
    print("Title :", data["Title"])
    print("Year  :", data["Year"])
    print("Rating:", data["imdbRating"])
else:
    print("❌ Movie Not Found.")    