from flask import Flask
from routes.index_routes import index_blueprint
from routes.browse_routes import browse_blueprint
from routes.error_routes import error_blueprint
from routes.login_routes import login_blueprint
import data, menuData

app = Flask(__name__)

def get_theme_css():
    # Implement logic to retrieve the user's theme preference and return the corresponding CSS path
    theme_preference = "light"  # Replace with your actual logic
    return f"static/{theme_preference}_theme.css"
    
# Register the Blueprints from separate files
app.register_blueprint(index_blueprint)
app.register_blueprint(browse_blueprint)
app.register_blueprint(error_blueprint)
app.register_blueprint(login_blueprint)

if __name__ == '__main__':
    app.run()
