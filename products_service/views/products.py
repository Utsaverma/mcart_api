from flask import jsonify, request
from flask_restx import Namespace, Resource

from controller.search import search_by_title


NS = Namespace('search', description="Get data for the pricing list")


@NS.route('')
class Products(Resource):
    """Handles the listing of the products"""

    def post(self,):
        """Returns the list of properties"""
        data = request.json
        key = data.get('key')
        start_index = data.get('start', 0)
        size = data.get('size', 20)
        filters = data.get('filters')
        return jsonify(search_by_title(key, start_index, size, filters))
