from flask import Blueprint, render_template, request
import menuData,data
from .theme import theme_selection

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/',endpoint='index')
def index():
    trending = menuData.trending

    
    return render_template('index.html', trending=trending, theme_css=theme_selection())
