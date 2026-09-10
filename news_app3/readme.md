# 📰 News Headlines App

A simple **News Headlines App** built using **Python (Flask)**, **HTML**, and **CSS**. Users can enter any news topic, and the app fetches the **top 5 latest news headlines** using the **NewsAPI**.

## ✨ Features

* 🔍 Search news by topic.
* 📰 Displays the top 5 latest headlines.
* ⚡ Fast and simple user interface.
* ❌ Shows **"No News"** if no articles are found.

## 🛠️ Technologies Used

* Python
* Flask
* HTML5
* CSS3
* NewsAPI

## 📁 Project Structure

```text
news-headlines-app/
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
cd news-headlines-app
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

1. Enter a news topic (Example: *Technology*, *Sports*, *India*).
2. Click the **Search** button.
3. The app sends a request to **NewsAPI**.
4. Flask receives the latest news data.
5. The top 5 headlines are displayed on the webpage.

## 📷 Example

**Input:**

```text
Technology
```

**Output:**

* AI launches new features.
* Apple announces latest iPhone.
* SpaceX completes new mission.
* Google releases Android update.
* Microsoft introduces AI tools.

## 📚 API Used

This project uses the **NewsAPI** to fetch live news headlines based on the user's search topic.

## 👩‍💻 Author

**Vanamala Jayasurya**

Python Mini Project — News Headlines App using Flask and NewsAPI.
