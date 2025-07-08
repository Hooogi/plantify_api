from flask import Blueprint, jsonify, current_app, request, Response
from .endpoint_configs import ENDPOINT_CONFIGS
from .services import handle_db_action

endpoints_blueprint = Blueprint('endpoint', __name__)

@endpoints_blueprint.route("/ping")
def ping():
    return jsonify({"message": "API is running!"})

@endpoints_blueprint.route("/<type>/<endpoint>", methods=["GET"])
def dispatch(type,endpoint):
    params = request.args.to_dict()
    supported_types = {"json", "insert", "update", "delete"}

    if type not in supported_types:
        return Response("Invalid type", status=404)
    if endpoint not in ENDPOINT_CONFIGS:
        return Response("Invalid endpoint", status=404)

    return handle_db_action(endpoint, params, type)





