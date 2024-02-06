
from flask import jsonify, request
from flask_restx import Namespace, Resource

from controller.search import search_by_category

NS = Namespace('searchByCategory', description="Get list of products by category")


@NS.route('')
class ProductsSearchByCategory(Resource):
    """Return the list of products by Category"""

    def get(self):
        category = request.args.get('category')
        size = request.args.get('size')
        start_index = request.args.get('start')
        return jsonify(search_by_category(category, size, start_index))
