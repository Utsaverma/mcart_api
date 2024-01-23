# product-service/util.py
import os

import boto3
from flask import Flask, request, jsonify
import pandas as pd
from controller.search import search_by_title, search_by_id

app = Flask(__name__)

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


@app.route('/search', methods=['GET'])
def get_search_data():
    param1 = request.args.get('key')
    return jsonify(search_by_title(param1))

@app.route('/searchById', methods=['GET'])
def get_search_by_id():
    param1 = request.args.get('id')
    return jsonify(search_by_id(param1))


if __name__ == '__main__':
    app.run(port=5000)
