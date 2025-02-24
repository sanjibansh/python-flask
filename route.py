from flask import request, Blueprint, jsonify
from service import process_leave_request_service, get_leave_request_service

api_routes = Blueprint("api_routes", __name__)

@api_routes.route('/api/v1/leave_request', methods=["POST"])
def leave_request():
    data = request.json  # Expecting JSON payload
    response, status_code = process_leave_request_service(data)
    return jsonify(response), status_code

@api_routes.route('/api/v1/leave_requests/<int:id>', methods=["GET"])
def get_leave_request(id):
    return jsonify(get_leave_request_service(id))
