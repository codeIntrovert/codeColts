from flask import Flask
from routes.index_routes import index_blueprint
from routes.browse_routes import browse_blueprint
from routes.error_routes import error_blueprint
from routes.login_routes import login_blueprint
from routes.view_routes import view_blueprint


app = Flask(__name__)

# Register the Blueprints from separate files
app.register_blueprint(index_blueprint)
app.register_blueprint(browse_blueprint)
app.register_blueprint(error_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(view_blueprint)

if __name__ == '__main__':
    app.run()
