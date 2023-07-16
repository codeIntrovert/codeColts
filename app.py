from flask import Flask, render_template
import data
app = Flask(__name__)

@app.route('/')
def index():
    beginner = data.beginner
    lecturesData = data.lecturesData
    return render_template('index.html', beginner=beginner, lecturesData=lecturesData )

@app.route('/browse')
def browse():
    beginner = data.beginner
    advance = data.advance
    return render_template('browse.html', beginner=beginner, advance=advance)

@app.route('/myCourses')
def myCourses():
    #pass course details here
    return render_template('details.html')

@app.route('/details')
def details():
    course = data.course
    lecturesData = data.lecturesData
    return render_template('details.html', course=course, lecturesData=lecturesData)

@app.route('/profile')
def profile():
    return render_template('profile.html' )

@app.route('/login')
def login():
    return render_template('login.html')

def page_not_found(e):
    error = e
    return render_template('error.html', errorCode=error), 404

if __name__ == '__main__':
    app.run()
