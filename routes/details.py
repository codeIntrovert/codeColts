# Description: This file renders the details page for a course.
from flask import render_template, request
import data, menuData
from lecturesData import lecturesData
from .course_mapping import course_mapping

def course_detail(course_name):
    theme_preference = request.cookies.get('theme', 'light')
    theme_css = theme_preference + "_theme"

    if course_name not in course_mapping:
        return render_template('components/error.html', theme_css=theme_css)

    course = course_mapping[course_name]
    lectures_data = lecturesData.get(course_name, [])
    trending = menuData.trending

    return render_template('details.html', course=course, lectures_data=lectures_data, trending=trending, theme_css=theme_css)
