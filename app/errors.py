from flask import render_template
from app import app

@app.errorhandler(404) 
def invalid_route(error): 
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def not_autorized(error):
    return render_template('errors/403.html'), 403

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500
        