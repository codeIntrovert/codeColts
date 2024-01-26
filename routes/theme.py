from flask import request



def theme_selection():
    theme_preference = request.cookies.get('theme', 'light')  # Default to 'light' if cookie not found
    return theme_preference + "_theme" 