from flask import Blueprint, render_template, request


view_blueprint = Blueprint('view', __name__)

@view_blueprint.route('/view')
def login():
    theme_preference = request.cookies.get('theme', 'light')  # Default to 'light' if cookie not found
    theme_css = theme_preference + "_theme"  # Assuming your CSS files are named "light_theme.css" and "dark_theme.css
    
    return render_template('view.html', theme_css=theme_css)
