from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movie_names

@app.route('/')
def home():
    movie_list = movies['title'].values
    return render_template('index.html', movie_list=movie_list, recommendations=[])

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    selected_movie = request.form['movie']
    recommendations = recommend(selected_movie)
    movie_list = movies['title'].values
    return render_template('index.html', movie_list=movie_list, recommendations=recommendations, selected_movie=selected_movie)

if __name__ == "__main__":
    app.run(debug=True)
