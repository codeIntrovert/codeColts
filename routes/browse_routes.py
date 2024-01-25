from flask import Blueprint, render_template, redirect, url_for, request
import data, menuData
from lecturesData import lecturesData
from .details import course_detail
from .course_mapping import course_mapping

browse_blueprint = Blueprint('browse', __name__)

################### General /browse page ###################
@browse_blueprint.route('/browse', endpoint='browse_home', methods=['GET', 'POST'])
def browse():
    trending = menuData.trending
    allCourses = menuData.all
    theme_preference = request.cookies.get('theme', 'light')  # Default to 'light' if cookie not found
    theme_css = theme_preference + "_theme"
    
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




#Details of courses @ browese/python etc [DO NOT CHANGE]
@browse_blueprint.route('/browse/<course_name>', endpoint='browse_details')
def browse_details(course_name):
    # Call the details function here
    return course_detail(course_name)

