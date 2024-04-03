from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)

# Preprocessing Data
# Assuming 'movies.csv' and 'credits.csv' are in the same directory as your Flask app
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')
movies = movies.merge(credits, on='title')
# Include all preprocessing steps here, such as feature extraction and similarity calculation

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movies_list:
        recommendations.append(new_df.iloc[i[0]].title)
    return recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def get_recommendations():
    movie_name = request.args.get('movie')
    recommendations = recommend(movie_name)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
