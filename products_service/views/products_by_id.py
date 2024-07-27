
from flask import jsonify, request
from flask_restx import Namespace, Resource

from controller.search import search_by_id

NS = Namespace('searchById', description="Get data for the particular product")


@NS.route('')
class ProductsSearchById(Resource):
    """Return the product by Id"""

    def get(self):
        """Returns the list of properties"""
        param1 = request.args.get('id')
        return jsonify(search_by_id(param1))
