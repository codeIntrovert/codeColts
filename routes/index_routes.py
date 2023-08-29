from flask import Blueprint, render_template, request
import menuData,data


index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/',endpoint='index')
def index():
    trending = menuData.trending
    theme_preference = request.cookies.get('theme', 'light')  # Default to 'light' if cookie not found
    theme_css = theme_preference + "_theme"  # Assuming your CSS files are named "light_theme.css" and "dark_theme.css
    
    return render_template('index.html', trending=trending, theme_css=theme_css)
