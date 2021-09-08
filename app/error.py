from flask import render_template
from app import app

@app.errorhandler(404)
def not_found_here(error):
    '''
    Render the 404 page
    '''
    return render_template('404.html'), 404