from flask import render_template
from app import app
from .request import get_movies, get_movie

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to the best Movie Review Webpage on the internet'
    return render_template('index.html', title=title, popular=popular_movies, upcoming=upcoming_movie, now_showing=now_showing_movie)

@app.route('/movies/<int:movie_id>')
def movies(movie_id):
    '''
    Returns movie page details
    '''
    title = 'Movie: '+str(movie_id)
    return render_template('movie.html', id=movie_id, title=title)

@app.route('/movie/<int:id>')
def movie(id):
    '''
    Single movie details
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html', title=title, movie=movie)