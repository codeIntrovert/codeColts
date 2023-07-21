from flask import Flask, render_template, redirect, url_for
import data

app = Flask(__name__)

@app.route('/')
def index():
    beginner = data.beginner
    lecturesData = data.lecturesData
    return render_template('index.html', beginner=beginner, lecturesData=lecturesData)

@app.route('/details/')
def details_default():
    # Redirect users to the /browse page when accessing /details/ without any parameters
    return redirect(url_for('browse'))

@app.route('/browse')
def browse():
    beginner = data.beginner
    advanced = data.advanced
    return render_template('browse.html', beginner=beginner, advanced=advanced)

@app.route('/details/<course_name>')
def details(course_name):
    # Map the course_name parameter to the corresponding course data using a dictionary
    course_mapping = {
        'java': data.Java,
        'csharp': data.CSharp,
        'reactjs': data.reactjs,
        'ml': data.ML,
        'js': data.JavaScript
        # Add more courses here as needed
    }

    # Check if the given course_name exists in the mapping, if not, return an error or redirect
    if course_name not in course_mapping:
        return render_template('components/error.html')

    # Get the corresponding course data from the course_mapping
    course = course_mapping[course_name]
    lecturesData = data.lecturesData
    beginner = data.beginner
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