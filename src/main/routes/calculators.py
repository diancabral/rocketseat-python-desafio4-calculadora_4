from http import HTTPStatus
from typing import cast
from src.errors.error_controller import handle_errors
from src.main.factories.calculator3 import calculator3_factory
from src.main.factories.calculator1 import calculator1_factory
from src.main.factories.calculator2 import calculator2_factory
from src.main.factories.calculator4 import calculator4_factory
from flask import Blueprint, jsonify, request

calc_route_bp = Blueprint('calc_routes', __name__)


@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    try:
        calc = calculator1_factory()
        response = calc.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)

        return jsonify(error_response['body']), cast(HTTPStatus, error_response['status_code'])


@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    try:
        calc = calculator2_factory()
        response = calc.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)

        return jsonify(error_response['body']), cast(HTTPStatus, error_response['status_code'])


@calc_route_bp.route("/calculator/3", methods=["POST"])
def calculator_3():
    try:
        calc = calculator3_factory()
        response = calc.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)

        return jsonify(error_response['body']), cast(HTTPStatus, error_response['status_code'])


@calc_route_bp.route("/calculator/4", methods=["POST"])
def calculator_4():
    try:
        calc = calculator4_factory()
        response = calc.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)

        return jsonify(error_response['body']), cast(HTTPStatus, error_response['status_code'])
