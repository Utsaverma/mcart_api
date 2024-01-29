import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.search import search_by_title, search_by_id, get_all_categories_util, \
    search_by_category

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def index():
#     df_categories = pd.read_csv(r'/Users/utsavverma/Downloads/amazon_categories.csv', sep=",")
#     df_products = pd.read_csv(r'/Users/utsavverma/Downloads/amazon_products.csv', sep=",")
#     df_final = pd.merge(df_products, df_categories, left_on='category_id', right_on='id', how='inner')[['asin', 'title', 'imgUrl', 'productURL', 'stars', 'reviews', 'price',
#        'listPrice', 'category_id', 'category_name', 'isBestSeller', 'boughtInLastMonth']]
#     df_final.to_csv(r'/Users/utsavverma/Downloads/mcart_products.csv', sep=",")
#     print(df_final)
#     print(df_final.columns)
#     # print(df_categories)
#     # print(df_products)
#     return 'Product Service'


# @app.route('/search', methods=['GET'])
# def get_search_data():
#     key = request.args.get('key')
#     start_index = request.args.get('start', 0)
#     size = request.args.get('size', 20)
#     return jsonify(search_by_title(key, start_index, size))


@app.route('/')
def index():
    return "success"

@app.route('/search', methods=['POST'])
def get_search_data():
    data = request.json

    key = data.get('key')
    start_index = data.get('start', 0)
    size = data.get('size', 20)
    filters = data.get('filters')
    return jsonify(search_by_title(key, start_index, size, filters))


@app.route('/searchById', methods=['GET'])
def get_search_by_id():
    param1 = request.args.get('id')
    return jsonify(search_by_id(param1))


@app.route('/searchByCategory', methods=['GET'])
def get_search_by_category():
    category = request.args.get('category')
    size = request.args.get('size')
    start_index = request.args.get('start')
    return jsonify(search_by_category(category, size, start_index))


@app.route('/getAllCategories', methods=['GET'])
def get_all_categories():
    return jsonify(get_all_categories_util())


if __name__ == '__main__':
    port = os.environ.get('PORT', '') if os.environ.get('PORT', '') else 5000
    app.run(host='0.0.0.0', port=port)
