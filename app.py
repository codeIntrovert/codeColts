from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route('/')
def index():
    beginner = data.beginner
    lecturesData = data.lecturesData
    return render_template('index.html', beginner=beginner, lecturesData=lecturesData)

@app.route('/browse')
def browse():
    beginner = data.beginner
    advanced = data.advanced
    return render_template('browse.html', beginner=beginner, advanced=advanced)

@app.route('/myCourses')
def myCourses():
    # pass course details here
    return render_template('details.html')

@app.route('/details')
def details():
    course = data.course
    lecturesData = data.lecturesData
    beginner = data.beginner
    advanced = data.advanced
    return render_template('details.html', course=course, lecturesData=lecturesData, beginner=beginner)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('components/error.html'), 404

if __name__ == '__main__':
    app.run()