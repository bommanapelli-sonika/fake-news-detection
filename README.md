# 📰 Fake News Detection System

## 📌 Overview
This project is a Machine Learning-based web application that detects whether a news article is Fake or Real using Natural Language Processing (NLP). It uses a trained ML model and is deployed using a Flask web application.

## 🚀 Features
- Detects Fake vs Real news
- Machine Learning classification model
- NLP preprocessing (TF-IDF Vectorization)
- Simple web UI using Flask + HTML
- Fast and easy prediction system

## 🛠️ Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- NLP (TF-IDF Vectorizer)
- HTML / CSS

## 📁 Project Structure
fake-news-detection/
├── app.py              # Flask web app
├── train.py            # Model training script
├── model.pkl           # Trained ML model
├── dataset/
│   └── news.csv
├── templates/
│   └── index.html
└── README.md

## ⚙️ Installation & Setup

### 1. Clone repository
git clone https://github.com/YOUR_USERNAME/fake-news-detection.git
cd fake-news-detection

### 2. Create virtual environment (optional)
python -m venv venv

Activate:
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Train model (if needed)
python train.py

### 5. Run Flask app
python app.py

### 6. Open browser
http://127.0.0.1:5000/

## 🧠 How it Works
1. Load dataset (news.csv)
2. Preprocess text using NLP
3. Convert text using TF-IDF
4. Train ML model
5. Save model as model.pkl
6. Flask predicts input news

## 📊 Output
Input: News text  
Output: FAKE / REAL

## 🎯 Future Improvements
- Improve accuracy using Deep Learning (LSTM / BERT)
- Deploy on cloud (Render / AWS / HuggingFace)
- Add live news scraping
- Show confidence score
- Improve UI design

## 👨‍💻 Author
Bommanapelli Sonika

## ⭐ Support
If you like this project, give a star ⭐
