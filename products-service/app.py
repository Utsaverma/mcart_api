# product-service/app.py

from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    df_categories = pd.read_csv(r'/Users/utsavverma/Downloads/amazon_categories.csv', sep=",")
    df_products = pd.read_csv(r'/Users/utsavverma/Downloads/amazon_products.csv', sep=",")
    df_final = pd.merge(df_products, df_categories, left_on='category_id', right_on='id', how='inner')[['asin', 'title', 'imgUrl', 'productURL', 'stars', 'reviews', 'price',
       'listPrice', 'category_id', 'category_name', 'isBestSeller', 'boughtInLastMonth']]
    df_final.to_csv(r'/Users/utsavverma/Downloads/mcart_products.csv', sep=",")
    print(df_final)
    print(df_final.columns)
    # print(df_categories)
    # print(df_products)
    return 'Product Service'

if __name__ == '__main__':
    app.run(port=5000)
