# order_service
import os
from datetime import datetime

from flask import Flask, jsonify, Blueprint
from flask_compress import Compress
from flask_cors import CORS
from flask_restx import Api
import settings

APP = Flask(__name__)
COMPRESS = Compress()

restx_blueprint = Blueprint('api', __name__, url_prefix='/mcart/v1/orders')
MCART_API = Api(restx_blueprint,
                version='1.0',
                title='MCART ORDERS RELATED API',
                description='A description of my orders API')


def configure_app(flask_app):
    """Configures flask application."""
    flask_app.config.from_object(os.environ.get('ENV_CONFIG'))
    flask_app.config['SQLALCHEMY_ECHO'] = True
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    """Initializes the flask application"""

    from views.orders import NS as ORDERS_NS
    from views.order_by_user import NS as ORDERS_BY_USER_NS

    configure_app(flask_app)
    CORS(flask_app)

    MCART_API.add_namespace(ORDERS_NS)
    MCART_API.add_namespace(ORDERS_BY_USER_NS)

    flask_app.register_blueprint(restx_blueprint)
    COMPRESS.init_app(flask_app)


@APP.route("/mcart/v1/orders/status", methods=["GET"])
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


@APP.after_request
def _after_request(response):
    response.headers["access-control-allow-headers"] = "*"
    response.headers["access-control-allow-methods"] = "*"
    response.headers["access-control-allow-origin"] = "*"
    return response


initialize_app(APP)


if __name__ == '__main__':
    port = os.environ.get('PORT', '') if os.environ.get('PORT', '') else settings.FLASK_SERVER_PORT
    APP.run(host='0.0.0.0', port=port)
