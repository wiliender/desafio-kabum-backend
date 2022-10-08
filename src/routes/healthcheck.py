from flask import Blueprint

route = Blueprint('healthcheck', __name__, url_prefix="/")

@route.route("/", methods=["GET"])  # type: ignore
def index():
    return 'Atividade Back-end Consulta Shipping', 200