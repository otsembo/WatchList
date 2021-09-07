from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to the best Movie Review Webpage on the internet'
    return render_template('index.html', title=title)

@app.route('/movies/<int:movie_id>')
def movie(movie_id):
    '''
    Returns movie page details
    '''
    title = 'Movie: '+str(movie_id)
    return render_template('movie.html', id=movie_id, title=title)