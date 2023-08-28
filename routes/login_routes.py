from flask import Blueprint, render_template, request


login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login')
def login():
    theme_preference = request.cookies.get('theme', 'light')  # Default to 'light' if cookie not found
    theme_css = f"static/assets/sass/{theme_preference}_theme.css"
    return render_template('login.html', theme_css=theme_css)
