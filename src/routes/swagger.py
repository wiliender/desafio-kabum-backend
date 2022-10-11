from flask import Blueprint, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

route = Blueprint('swagger', __name__, url_prefix="")

@route.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)

SWAGGER_URL= "/swagger"
API_URL="/static/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Seans-Python-Flask-REST"
    }
)
route.register_blueprint(swaggerui_blueprint, url_prefix= SWAGGER_URL)