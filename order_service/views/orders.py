from flask import jsonify, request
from flask_restx import Namespace, Resource

from controller.order import save_order


NS = Namespace('save', description="Save orders into dynamo table")


@NS.route('')
class Orders(Resource):
    """saves an order into dynamo"""

    def post(self,):
        """saves orders"""
        return jsonify(save_order(request.json))
