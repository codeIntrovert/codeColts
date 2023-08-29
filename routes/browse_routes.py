from flask import Blueprint, render_template, redirect, url_for, request
import data, menuData
from lecturesData import lecturesData


browse_blueprint = Blueprint('browse', __name__)

# Map the course_name parameter to the corresponding course data using a dictionary
course_mapping = {
    'Java': data.Java,
    'C++': data.cplusplus,
    'ReactJS': data.ReactJS,
    'ML+AI': data.ML,
    'JavaScript': data.JavaScript,
    'Django': data.Django,
    'Python': data.Python,
    'HTML': data.HTML,
    'Angular': data.Angular,
    'Android': data.Android,
    'NodeJS': data.NodeJS,
    'SQL': data.SQL,
    'PHP': data.PHP,
    'RubyOnRails': data.Rails,
    'VueJS': data.VueJS,
    'DataScience': data.DataScience,
    'Cybersecurity': data.Cybersecurity,
    'Swift': data.Swift,
    'Ruby': data.ruby,

    # Add more courses here as needed
}

@browse_blueprint.route('/browse/<course_name>', endpoint='browse_details')
def details(course_name):
    theme_preference = request.cookies.get('theme', 'light')  # Default to 'light' if cookie not found
    theme_css = theme_preference + "_theme"  # Assuming your CSS files are named "light_theme.css" and "dark_theme.css"

    # Check if the given course_name exists in the mapping, if not, return an error or redirect
    if course_name not in course_mapping:
        return render_template('components/error.html', theme_css=theme_css )

    # Get the corresponding course data from the course_mapping
    course = course_mapping[course_name]
    lectures_data = lecturesData.get(course_name, [])  # Get lectures data for the course

    trending = menuData.trending
    return render_template('details.html', course=course, lectures_data=lectures_data, trending=trending, theme_css=theme_css)

####################### details end #######################


################### General /browse page ###################
@browse_blueprint.route('/browse', endpoint='browse_home', methods=['GET', 'POST']) # used when no course_name is provided
def browse():
    trending = menuData.trending
    allCourses = menuData.all
    theme_preference = request.cookies.get('theme', 'light')  # Default to 'light' if cookie not found
    theme_css = theme_preference + "_theme"  # Assuming your CSS files are named "light_theme.css" and "dark_theme.css"
    
    # If the form is submitted (POST request), get the search keyword from the form
    if request.method == 'POST':
        search_keyword = request.form.get('searchKeyword')
        # Perform the search based on the search_keyword and filter the courses
        filtered_courses = []
        for course_name, course_data in course_mapping.items():
            if search_keyword.lower() in course_name.lower():
                filtered_courses.append(course_data)
        return render_template('browse.html',theme_css=theme_css, trending=trending, allCourses=allCourses, search_keyword=search_keyword, search_results=filtered_courses)
    
    # If it's a GET request, show the regular browse page without search results
    return render_template('browse.html', trending=trending, allCourses=allCourses, theme_css=theme_css)
