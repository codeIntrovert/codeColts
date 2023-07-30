from flask import Blueprint, render_template, redirect, url_for, request
import data, menuData

browse_blueprint = Blueprint('browse', __name__)

# Map the course_name parameter to the corresponding course data using a dictionary
course_mapping = {
    'Java': data.Java,
    'C#': data.CSharp,
    'ReactJS': data.reactjs,
    'ML+AI': data.ML,
    'JavaScript': data.JavaScript,
    'Django': data.Django
    # Add more courses here as needed
}

@browse_blueprint.route('/browse/<course_name>', endpoint='browse_details')
def details(course_name):

    # Check if the given course_name exists in the mapping, if not, return an error or redirect
    if course_name not in course_mapping:
        return render_template('components/error.html')

    # Get the corresponding course data from the course_mapping
    course = course_mapping[course_name]
    lecturesData = data.lecturesData
    beginner = menuData.beginner
    return render_template('details.html', course=course, lecturesData=lecturesData, beginner=beginner)

@browse_blueprint.route('/browse', endpoint='browse_home', methods=['GET', 'POST'])
def browse():
    beginner = menuData.beginner
    advanced = menuData.advanced

    # If the form is submitted (POST request), get the search keyword from the form
    if request.method == 'POST':
        search_keyword = request.form.get('searchKeyword')
        # Perform the search based on the search_keyword and filter the courses
        filtered_courses = []
        for course_name, course_data in course_mapping.items():
            if search_keyword.lower() in course_name.lower():
                filtered_courses.append(course_data)
        return render_template('browse.html', beginner=beginner, advanced=advanced, search_keyword=search_keyword, search_results=filtered_courses)
    
    # If it's a GET request, show the regular browse page without search results
    return render_template('browse.html', beginner=beginner, advanced=advanced)