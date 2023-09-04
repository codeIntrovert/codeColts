from flask import Flask, render_template, request, redirect, url_for, session, flash
from routes.index_routes import index_blueprint
from routes.browse_routes import browse_blueprint
from routes.login_routes import login_blueprint
from routes.view_routes import view_blueprint


app = Flask(__name__)

# Register the Blueprints from separate files
app.register_blueprint(index_blueprint)
app.register_blueprint(browse_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(view_blueprint)

@app.errorhandler(404)
def page_not_found(error):
    theme_preference = request.cookies.get('theme', 'light')  # Default to 'light' if cookie not found
    theme_css = theme_preference + "_theme"
    return render_template('components/error.html',theme_css=theme_css), 404

if __name__ == '__main__':
    app.run()
