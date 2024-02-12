# order_service_api
import os
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
import order_service_api.settings as settings

from order_service_api.controller.order import get_order_details_by_user_util, \
    save_order

from order_service_api.utilities.util import get_logger

app = Flask(__name__)
CORS(app)

API_PREFIX = '/mcart/v1/orders'

logger = get_logger()


@app.route(f"{API_PREFIX}/status", methods=["GET"])
def status():
    """
    Returns a simple message indicating the service is working as intended.
    """
    return jsonify(dict(
        status="healthy",
        serverTime=datetime.now(),
        version=settings.MCART_API_VERSION,
        notes="MCART ORDERS SERVICE RUNNING"
    ))


@app.route("/", methods=["GET"])
def check():
    """
    Returns a simple message indicating the service is working as intended.
    """
    return jsonify(dict(
        status="healthy",
        serverTime=datetime.now(),
        version=settings.MCART_API_VERSION,
        notes="MCART ORDERS SERVICE RUNNING"
    ))


@app.route(f"{API_PREFIX}/getOrderDetailsByUser",  methods=["GET"])
def get_order_details_by_user():
    """retrieves order deatils"""
    user_id = request.args.get('userId')
    logger.info(f"get_order_details_by_user is called with userid {user_id}")
    return jsonify(get_order_details_by_user_util(user_id))


@app.route(f"{API_PREFIX}/save", methods=["POST"])
def save():
    """saves orders"""
    logger.info(f"save order deatils with ")
    logger.info({request.json})
    return jsonify(save_order(request.json))


@app.after_request
def _after_request(response):
    response.headers["access-control-allow-headers"] = "*"
    response.headers["access-control-allow-methods"] = "*"
    response.headers["access-control-allow-origin"] = "*"
    return response


if __name__ == '__main__':
    port = os.environ.get('PORT', '') if os.environ.get('PORT', '') else 5000
    app.run(host='0.0.0.0', port=port)
