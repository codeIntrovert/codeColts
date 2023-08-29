from flask import Blueprint, render_template, request


login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login')
def login():
    theme_preference = request.cookies.get('theme', 'light')  # Default to 'light' if cookie not found
    theme_css = theme_preference + "_theme"  # Assuming your CSS files are named "light_theme.css" and "dark_theme.css
    
    return render_template('login.html', theme_css=theme_css)
