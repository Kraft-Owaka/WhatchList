from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title)

    # message = 'Hello World'
    # return render_template('index.html',message = message)


@app.route('/movie/<movie_id>')
def movie(movie_id):
    '''
    view movie page function that returns detailed page and its data
    '''
    title = f'You are viewing {movie_id}'
    return render_template('movie.html', title = title)