import streamlit as st
import pandas as pd
import pickle
import requests
import numpy as np
st.set_page_config(
    page_title="Movie Recommender 🎬",
    page_icon="🎬",
    layout="wide"
)
def fetch_poster(movie_id):

    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYzU2YWM1MzVhNDhmNTQ2ZTAzZDQyNWMxNWRkMTc5MCIsIm5iZiI6MTcyMDc3ODA4Ny43MTc5ODEsInN1YiI6IjY2ODRkZmM5ZGM3YTlhY2NjOTFhM2Y3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3qJoiB5AxjjQcCSYvGA2BNJcRMAAtPXWtBzCPCLbwRI"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

movies_list = pickle.load(open('moviesdict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity1 = pickle.load(open('similarity1.pkl', 'rb'))
similarity2 = pickle.load(open('similarity2.pkl', 'rb'))
similarity = np.vstack((similarity1, similarity2))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Outfit:wght@500;800&display=swap');

    /* Global Transitions & Variables */
    :root {
        primary-bg: #0e1117;
        secondary-bg: #1a1c23;
        accent-color: #ff4b4b; 
        text-color: #ffffff;
        card-bg: #262730;
    }

    /* Main Container Styling */
    .main {
        background-color: var(--primary-bg);
        color: var(--text-color);
        font-family: 'Inter', sans-serif;
    }

    /* Hide Streamlit Header/Footer for cleaner look */
    header, footer {
        visibility: hidden;
    }

    /* Title Styling */
    .main-title {
        font-family: 'Outfit', sans-serif;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        text-align: center;
        background: linear-gradient(45deg, #ff4b4b, #ff8a8a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    .sub-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        text-align: center;
        color: #a0a0a0;
        margin-bottom: 2rem;
    }

    /* Styling Selectbox & Buttons */
    div[data-baseweb="select"] {
        border-radius: 10px;
        background-color: var(--secondary-bg);
    }

    .stButton>button {
        width: 100%;
        background-color: var(--accent-color);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton>button:hover {
        background-color: #ff3333;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4);
        transform: translateY(-2px);
    }

    /* Movie Card Styling */
    .movie-card {
        background-color: var(--card-bg);
        border-radius: 15px;
        padding: 0px;
        margin-bottom: 20px;
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        overflow: hidden;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }

    .movie-card:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 30px rgba(0,0,0,0.5);
    }

    .movie-poster {
        width: 100%;
        border-radius: 15px 15px 0 0;
        object-fit: cover;
    }

    .movie-title-card {
        padding: 12px;
        text-align: center;
        font-weight: 700;
        font-size: 0.9rem;
        color: #e0e0e0;
        min-height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Column Spacing */
    [data-testid="column"] {
        padding: 10px;
    }

</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🎬 Movie Recommender System</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Find Your Next Cinematic Adventure</p>', unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    'Which movie Did You Enjoy ?',
    movies['title'].values
)

if st.button('Get Recommendations'):
    names, posters = recommend(selected_movie_name)
    
    for row in range(2):
        cols = st.columns(3)
        for idx in range(3):
            movie_idx = row * 3 + idx
            with cols[idx]:
                st.markdown(f"""
                <div class="movie-card">
                    <img class="movie-poster" src="{posters[movie_idx]}">
                    <div class="movie-title-card">{names[movie_idx]}</div>
                </div>
                """, unsafe_allow_html=True)