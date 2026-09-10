# 🌦️ Atmosphere Weather App

A modern **Weather App** built with **Python (Flask)**, **HTML**, **CSS**, and **JavaScript**. Users can search for any city and get real-time weather information using the **OpenWeatherMap API**.

## ✨ Features

* 🔍 Search weather by city name.
* 🌡️ Shows current temperature in Celsius.
* ☁️ Displays weather condition and description.
* 💧 Shows humidity percentage.
* 🌬️ Displays wind speed.
* 🎨 Background changes automatically based on weather conditions (Clear, Rain, Clouds, Snow, Thunder, Mist, etc.).
* ❌ Displays an error message for invalid city names.

## 🛠️ Technologies Used

* Python
* Flask
* HTML5
* CSS3
* JavaScript
* OpenWeatherMap API

## 📁 Project Structure

```text
weather-app/
│── app.py          # Flask backend
│── index.html      # Frontend page
│── style.css       # Styling
│── README.md       # Project documentation
```

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-link>
```

### 2. Open the project folder

```bash
cd weather-app
```

### 3. Install required packages

```bash
pip install flask requests
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

```text
http://127.0.0.1:5000
```

## 🚀 How It Works

1. Enter a city name.
2. Click the **Search** button.
3. The app sends a request to the Flask backend.
4. Flask fetches live weather data from the OpenWeatherMap API.
5. The app displays temperature, weather condition, humidity, wind speed, and updates the background theme.

## 📷 Example

**Input**

```text
Hyderabad
```

**Output**

* 🌡️ Temperature: **28°C**
* ☁️ Condition: **Clouds**
* 📝 Description: **Broken Clouds**
* 💧 Humidity: **72%**
* 🌬️ Wind Speed: **3.5 m/s**

## 🌍 API Used

This project uses the **OpenWeatherMap API** to fetch real-time weather data for cities around the world.

## 👩‍💻 Author

**Vanamala Jayasurya**

Python Mini Project — Atmosphere Weather App using Flask and OpenWeatherMap API.
