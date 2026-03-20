Movie Recommender System
Overview
This repository contains a Streamlit-based web application for recommending movies based on a selected movie. The application uses a pre-trained similarity model and displays recommended movies along with their posters.

Features
Select a movie from a list to get recommendations.
Displays the recommended movies with their posters.
Utilizes The Movie Database (TMDb) API to fetch movie posters.
Requirements
Python 3.6 or higher
Streamlit
Pandas
Requests
Pickle
Numpy
Installation
Clone the repository:

Install the required packages:

pip install streamlit pandas requests numpy
Ensure you have the required pickle files (moviesdict.pkl, similarity1.pkl, similarity2.pkl) in the repository directory.

Usage
Run the Streamlit app:

streamlit run app.py
Open the provided URL in your web browser to access the application.

Select a movie from the dropdown menu and click the "Recommend" button to get recommendations.

File Descriptions
app.py: Main script for running the Streamlit app.
moviesdict.pkl: Pickle file containing movie data.
similarity1.pkl and similarity2.pkl: Pickle files containing pre-trained similarity matrices.
API Key
The application uses The Movie Database (TMDb) API to fetch movie posters. The API key is included in the script. Make sure to replace it with your own API key if necessary.

How It Works
The user selects a movie from the dropdown menu.
Upon clicking the "Recommend" button, the app fetches similar movies using the pre-trained similarity model.
The app then retrieves the posters of the recommended movies using the TMDb API.
The recommended movies and their posters are displayed on the web interface.
Acknowledgements
Streamlit
Pandas
The Movie Database (TMDb) API
Numpy
