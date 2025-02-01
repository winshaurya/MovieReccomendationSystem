import streamlit as st
import pickle as pp
import pandas as pd
import requests
from functools import lru_cache



def fetch_poster(movie_id):
    base_url = "https://api.themoviedb.org/3/movie/"
    image_base_url = "https://image.tmdb.org/t/p/w500"
    api_key = "6419fe3f0fcbbac100aa42b10e5d61d7"  
    url = f"{base_url}{movie_id}?api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"{image_base_url}{poster_path}"
    except requests.exceptions.RequestException as e:
        st.error(f" {movie_id}: {e}")
    return "https://via.placeholder.com/500x750?text=No+Image+Available"


def recommend(movie):
    mov_index = movies[movies['title'] == movie].index[0]
    distances = sim[mov_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:31]
                                                                                    
    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters


movies_dict = pp.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
sim = pp.load(open('sim.pkl', 'rb'))

# UI
st.title("🎥 Movie Recommendation")

option = st.selectbox("Select a movie:", movies['title'].values)

if st.button('Recommend'):
    recommendations, posters = recommend(option)
    num_columns = 5
    columns = st.columns(num_columns)
    for index, (title, poster) in enumerate(zip(recommendations, posters)):
        col = columns[index % num_columns]
        with col:
            if poster:
                st.image(poster, width=280)
            st.markdown(
                f"<div style='text-align: center; font-size: 16px; font-weight: bold;'>{title}</div>",
                unsafe_allow_html=True,
            )
