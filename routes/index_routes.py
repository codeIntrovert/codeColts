from flask import Blueprint, render_template
import menuData,data

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/',endpoint='index')
def index():
    beginner = menuData.beginner
    lecturesData = data.watchHistory
    return render_template('index.html', beginner=beginner, lecturesData=lecturesData)
