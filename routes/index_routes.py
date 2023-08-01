from flask import Blueprint, render_template
import menuData,data

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/',endpoint='index')
def index():
    trending = menuData.trending
    lecturesData = data.watchHistory
    return render_template('index.html', trending=trending, lecturesData=lecturesData)
