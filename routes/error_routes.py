from flask import Blueprint, render_template

error_blueprint = Blueprint('error', __name__)

@error_blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('components/error.html'), 404
