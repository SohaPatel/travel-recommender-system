# 🌍 Travel Recommendation System

This project is a **hybrid travel recommendation system** that suggests destinations based on user preferences and behavior. It combines **Content-Based Filtering** and **Collaborative Filtering** to provide more accurate and personalized recommendations.

---

## 🚀 Features

- 🔎 Content-Based Recommendation (based on user preferences)
- 👥 Collaborative Filtering (based on similar users)
- ⚡ Hybrid Recommendation (combines both approaches)
- 🌐 Flask API for backend
- 📊 Real-time recommendations via API endpoints

---

## 🧠 How It Works

### 1. Content-Based Filtering
Recommends destinations based on:
- Place category (beach, heritage, etc.)
- User interest (nature, history, etc.)
- Season and crowd preferences

---

### 2. Collaborative Filtering
- Uses user-item interaction matrix
- Finds similar users
- Recommends destinations liked by similar users

---

### 3. Hybrid Model
- Combines both methods using weighted scoring
- Formula:


Hybrid Score = α × Content Score + (1 − α) × Collaborative Score


---

## 🛠️ Tech Stack

- Python
- Flask
- Pandas, NumPy
- Scikit-learn (for similarity calculations)
- REST API

---

## 📂 Project Structure


travel-recommender/
│
├── api/ # Flask API
├── data/ # Dataset (processed + simulated)
├── src/ # Recommendation logic
│ ├── recommenders/
│ ├── utils/
│
├── run_api.py # Run backend server
├── run_content_based.py
├── run_collaborative.py
├── run_hybrid.py


---

## ⚙️ How to Run

### 1. Clone the repository


git clone https://github.com/SohaPatel/travel-recommender-system.git

cd travel-recommender-system


---

### 2. Install dependencies


pip install -r requirements.txt


---

### 3. Run the API


python run_api.py


Server runs on:

http://127.0.0.1:5000


---

## 📡 API Endpoints

### 🔹 Health Check

GET /api/health


---

### 🔹 Content-Based Recommendation

POST /api/recommend/manual


---

### 🔹 Collaborative Filtering

POST /api/recommend/collaborative


---

### 🔹 Hybrid Recommendation

POST /api/recommend/hybrid


---

## 📊 Sample Input (JSON)


{
"place_category": "beach",
"interest": "nature",
"best_season_to_visit": "winter",
"people": 2,
"top_n": 5,
"alpha": 0.6
}


---

## 📌 Output

- List of recommended destinations
- Includes:
  - City, State
  - Latitude & Longitude
  - Recommendation Scores

---

## ⚠️ Limitations

- Uses synthetic user ratings (no real user data)
- Static dataset (no real-time updates)
- Recommendations limited to dataset features

---

## 🔮 Future Improvements

- Real user interaction data
- Image-based recommendations
- NLP-based preference extraction
- Deployment on cloud (AWS / Render)
---

## 📌 Note

This project was developed as part of an academic coursework to demonstrate recommendation system techniques and hybrid modeling.
