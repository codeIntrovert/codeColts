from flask import Blueprint, render_template, redirect, url_for
import data, menuData

browse_blueprint = Blueprint('browse', __name__)

@browse_blueprint.route('/browse', endpoint='browse_home')
def browse():
    beginner = menuData.beginner
    advanced = menuData.advanced
    return render_template('browse.html', beginner=beginner, advanced=advanced)

@browse_blueprint.route('/browse/<course_name>', endpoint='browse_details')
def details(course_name):
    # Map the course_name parameter to the corresponding course data using a dictionary
    course_mapping = {
        'Java': data.Java,
        'C#': data.CSharp,
        'ReactJS': data.reactjs,
        'ML+AI': data.ML,
        'JavaScript': data.JavaScript
        # Add more courses here as needed
    }

    # Check if the given course_name exists in the mapping, if not, return an error or redirect
    if course_name not in course_mapping:
        return render_template('components/error.html')

    # Get the corresponding course data from the course_mapping
    course = course_mapping[course_name]
    lecturesData = data.lecturesData
    beginner = menuData.beginner
    return render_template('details.html', course=course, lecturesData=lecturesData, beginner=beginner)
