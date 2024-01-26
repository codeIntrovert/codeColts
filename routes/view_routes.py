from flask import Blueprint, render_template, request
from .theme import theme_selection

view_blueprint = Blueprint('view', __name__)

@view_blueprint.route('/view')
def views():
    
    link = request.args.get('link')
    thumbnail = request.args.get('thumbnail')
    topic = request.args.get('topics')
    courseName = request.args.get('courseName')
    video_link = request.args.get('video_link')

    return render_template('view.html', theme_css=theme_selection(), VIDEO_ID=link, thumbnail=thumbnail, topic=topic, courseName=courseName, video_link=video_link)
