from flask import Blueprint, request, jsonify
from src.controllers.search_controller import SearchController
calculator_routes_bp = Blueprint("api_routes", __name__)

from src.main.adapter.request_adapter import request_adapter
from src.main.validate.validation import Validation
from src.controllers.insert_controller import InsertController


@calculator_routes_bp.route("/insert", methods=["POST"])
def inserir():
    http_request = request_adapter(request)
    insControl = InsertController()
    http_response = insControl.retorno_http(http_request)        
    return jsonify(http_response.body), http_response.status_code

@calculator_routes_bp.route("/search", methods=["GET"])
def buscar():
    http_request = request_adapter(request)
    searchControl = SearchController()
    http_response = searchControl.retorno_http(http_request)        
    return jsonify(http_response.body), http_response.status_code
