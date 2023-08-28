from flask import Blueprint, render_template,request


error_blueprint = Blueprint('error', __name__)

@error_blueprint.errorhandler(404)
def page_not_found(e):
    theme_preference = request.cookies.get('theme', 'light')  # Default to 'light' if cookie not found
    theme_css = f"static/assets/sass/{theme_preference}_theme.css"
    return render_template('components/error.html', theme_css=theme_css), 404
