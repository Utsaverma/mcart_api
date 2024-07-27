from opensearchpy import Document, Text, Integer, Float, Boolean


class Product(Document):
    asin = Text()
    title = Text()
    img_url = Text()
    product_url = Text()
    stars = Float()
    reviews = Integer()
    price = Float()
    list_price = Float()
    sub_category_id = Integer()
    sub_category_name = Text()
    category_name = Text()
    is_best_seller = Boolean()
    bought_in_last_month = Integer()
    gender = Text()

    class Index:
        name = 'mcart-products'

    def save(self, ** kwargs):
        return super(Product, self).save(** kwargs)


def to_dict(document):
    return {
        "asin": document["asin"],
        "title": document["title"],
        "img_url": document["imgUrl"],
        "product_url": document["productURL"],
        "stars": document["stars"],
        "reviews": document["reviews"],
        "price": document["price"],
        "list_price": document["listPrice"],
        "sub_category_id": document["sub_category_id"],
        "sub_category_name": document["sub_category"],
        "category_name": document["category"],
        "is_best_seller": document["isBestSeller"],
        "bought_in_last_month": document["boughtInLastMonth"],
        "gender": document["gender"]
    }
