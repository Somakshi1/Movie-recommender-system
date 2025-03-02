# 🎬 Movie Recommender System

Welcome to the **Movie Recommender System**! This project uses machine learning techniques to recommend movies based on user preferences. Built with **Flask, Pandas, Numpy, and Scikit-learn**, this system provides personalized recommendations based on movie similarity.

![image](https://github.com/user-attachments/assets/930536dc-deb1-4767-94f8-5db5a4e5afb4)


## 📌 Features
- 🎥 **Content-Based Filtering**: Recommends movies similar to the one selected by the user.
- 🔍 **Search Functionality**: Find movies by title.
- 🎭 **Interactive Web Interface**: Built using Flask for easy user interaction.
- 📊 **Machine Learning Model**: Uses TF-IDF and cosine similarity for recommendations.

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Somakshi1/Movie-recommender-system.git
cd Movie-recommender-system
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App
```bash
python app.py
```
The application will run at `http://127.0.0.1:5000/`.

## 🛠 How It Works
1. The dataset is preprocessed to extract movie features.
2. A similarity matrix (cosine similarity) is computed using **TF-IDF Vectorization**.
3. The system recommends movies based on the selected movie's similarity score.
4. The web interface allows users to search for movies and get recommendations instantly.

## 📁 Project Structure
```
Movie-Recommender-System/
│── static/              # CSS & JS files
│── templates/           # HTML templates
│── app.py               # Flask application
│── movie_dataset.csv    # Dataset containing movie details
│── similarity.pkl       # Precomputed similarity matrix
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

## ⚠ Handling Large Files
The `similarity.pkl` file exceeds GitHub's size limit. To use it:
1. **Download it from Google Drive** (link to be added)
2. Place it in the project directory manually.

Alternatively, modify `app.py` to download it automatically using `gdown`:
```python
import gdown

gdown.download('GOOGLE_DRIVE_LINK', 'similarity.pkl', quiet=False)
```

## 🎯 Future Improvements
- 🔥 **Hybrid Recommendation (Content + Collaborative Filtering)**
- 📡 **Deploying to Render or Heroku**






