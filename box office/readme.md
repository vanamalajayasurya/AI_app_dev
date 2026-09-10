# 🎬 Movie Finder App

A simple **Movie Finder** web application built with **Python (Flask)**, **HTML**, **CSS**, and **JavaScript**. Search for any movie title and instantly get its **IMDb rating**, **release year**, and **movie poster** using the **OMDb API**.

## 📌 Features

* 🔍 Search movies by title.
* ⭐ View IMDb rating.
* 📅 View movie release year.
* 🖼️ Display movie poster.
* ❌ Shows **"Not Found"** message for invalid movie titles.
* 🎟️ Attractive Box Office ticket-style UI.

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **JavaScript**
* **OMDb API**

## 📁 Project Structure

```text
movie-finder/
│── app.py          # Flask backend
│── index.html      # Frontend page
│── style.css       # Styling
│── README.md       # Project documentation
```

## ▶️ How to Run the Project

1. Clone the repository.

```bash
git clone <your-github-repo-link>
```

2. Go to the project folder.

```bash
cd movie-finder
```

3. Install the required package.

```bash
pip install flask requests
```

4. Run the Flask app.

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🎥 How It Works

1. Enter a movie name.
2. Click **Search**.
3. The app sends a request to the Flask backend.
4. Flask fetches movie details from the **OMDb API**.
5. The movie ticket is displayed with the title, year, IMDb rating, and poster.

## 📷 Example Output

* Movie Title: **Inception**
* Year: **2010**
* IMDb Rating: **8.8**
* Poster displayed on the ticket.

## 👩‍💻 Author

**Vanamala Jayasurya**

Python Mini Project – Movie Finder using Flask and OMDb API.
