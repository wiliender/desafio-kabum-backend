from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest
from schemas.shipping import Payload
from data.companies import get

route = Blueprint('api', __name__, url_prefix="/v1")

@route.route("/shipping", methods=["POST"])
def index():
    try:
        pl = request.get_json(force=True)
        if not pl:
            raise BadRequest
        data = Payload().load(pl)
    except ValidationError as err:
        return jsonify({"error": "fail to validate, missing information"}), 400

    except BadRequest as err:
        return jsonify({"error": err.get_body()}), 400  # type: ignore

    return jsonify(get(
        width=data['dimension']['width'],  # type: ignore
        height=data['dimension']['height'],  # type: ignore
        weight=data['weight'],  # type: ignore
    )), 201