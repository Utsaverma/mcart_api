
from flask import jsonify
from flask_restx import Resource, Namespace

from controller.search import get_all_categories_util

NS = Namespace('getAllCategories', description="Get all categories")


@NS.route('')
class ProductCategories(Resource):
    """Return all categories"""

    def get(self):
        """Returns all existing categories """
        return jsonify(get_all_categories_util())
