from flask import Blueprint, render_template, request
from .theme import theme_selection

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login')
def login():
    
    return render_template('login.html', theme_css=theme_selection())
