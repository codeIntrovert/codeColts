from flask import Blueprint, render_template, request


view_blueprint = Blueprint('view', __name__)

@view_blueprint.route('/view')
def views():
    theme_preference = request.cookies.get('theme', 'light')  # Default to 'light' if cookie not found
    theme_css = theme_preference + "_theme"  # Assuming your CSS files are named "light_theme.css" and "dark_theme.css
    
    link = request.args.get('link')
    thumbnail = request.args.get('thumbnail')
    topic = request.args.get('topics')
    courseName = request.args.get('courseName')
    video_link = request.args.get('video_link')

    return render_template('view.html', theme_css=theme_css, VIDEO_ID=link, thumbnail=thumbnail, topic=topic, courseName=courseName, video_link=video_link)
