# order-service
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.order import get_order_details_by_user_util, save_order

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "success"
@app.route('/getOrderDetailsByUser', methods=['GET'])
def get_order_details_by_user():
    user_id = request.args.get('userId')
    return jsonify(get_order_details_by_user_util(user_id))

@app.route('/save', methods=['POST'])
def save_order_details():
    return jsonify(save_order(request.json))



if __name__ == '__main__':
    port = os.environ.get('PORT', '') if os.environ.get('PORT', '') else 5001
    app.run(host='0.0.0.0', port=port)
