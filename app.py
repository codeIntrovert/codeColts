from flask import Flask, render_template, request, redirect, url_for, session, flash, Response
from routes.index_routes import index_blueprint
from routes.browse_routes import browse_blueprint
from routes.login_routes import login_blueprint
from routes.view_routes import view_blueprint
from routes.theme import theme_selection


app = Flask(__name__)

# Register the Blueprints from separate files
app.register_blueprint(index_blueprint)
app.register_blueprint(browse_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(view_blueprint)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('components/error.html',theme_css=theme_selection()), 404

@app.route('/sitemap.xml')
def sitemap():
    try:
        with open('sitemap.xml', 'r') as f:
            sitemap_content = f.read()
        return Response(sitemap_content, content_type='application/xml')
    except FileNotFoundError:
        return "Sitemap not found", 404

if __name__ == '__main__':
    app.run()
