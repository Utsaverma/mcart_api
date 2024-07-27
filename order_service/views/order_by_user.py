from flask import jsonify, request
from flask_restx import Namespace, Resource

from controller.order import get_order_details_by_user_util


NS = Namespace('getOrderDetailsByUser', description="get order by user")


@NS.route('')
class OrdersByUser(Resource):
    """saves an order into dynamo"""

    def get(self,):
        """saves orders"""
        user_id = request.args.get('userId')
        return jsonify(get_order_details_by_user_util(user_id))
