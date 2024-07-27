import os
from datetime import datetime

from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from flask_restx import Api
import settings

APP = Flask(__name__)

restx_blueprint = Blueprint('api', __name__, url_prefix='/mcart/v1/products')
MCART_API = Api(restx_blueprint,
                version='1.0',
                title='MCART PRODUCTS RELATED API',
                description='A description of my products API')


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

    from views.products import NS as PRODUCTS_NS
    from views.products_by_id import NS as PRODUCTS_SEARCH_BY_ID_NS
    from views.products_by_category import NS as PRODUCTS_SEARCH_BY_CATEGORY_NS
    from views.product_categories import NS as PRODUCT_CATEGORIES_NS

    configure_app(flask_app)
    CORS(flask_app)

    MCART_API.add_namespace(PRODUCTS_NS)
    MCART_API.add_namespace(PRODUCTS_SEARCH_BY_ID_NS)
    MCART_API.add_namespace(PRODUCTS_SEARCH_BY_CATEGORY_NS)
    MCART_API.add_namespace(PRODUCT_CATEGORIES_NS)

    flask_app.register_blueprint(restx_blueprint)


@APP.route("/mcart/v1/products/status", methods=["GET"])
def status():
    """
    Returns a simple message indicating the service is working as intended.
    """
    return jsonify(dict(
        status="healthy",
        serverTime=datetime.now(),
        version=settings.MCART_API_VERSION,
        notes="MCART PRODUCTS SERVICE RUNNING"
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
