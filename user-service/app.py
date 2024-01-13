# product-service/app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'User Service'

if __name__ == '__main__':
    app.run(port=5002)
