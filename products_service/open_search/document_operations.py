import logging

from opensearchpy import Search, Q
from opensearchpy.helpers.aggs import Composite, Terms

from .product_model import Product, to_dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DocumentOperations:
    def __init__(self, opensearch_client, index_name):
        self.opensearch_client = opensearch_client
        self.index_name = index_name
        self.search_client = Search(using=self.opensearch_client, index=self.index_name)

    def insert_bulk(self, query):
        self.opensearch_client.bulk(query)

    def index_document(self, document_id, curr_doc):
        try:
            document = Product(
                meta={'id': curr_doc['asin']},
                asin=curr_doc['asin'],
                title=curr_doc['title'],
                img_url=curr_doc['imgUrl'],
                product_url=curr_doc['productURL'],
                stars=curr_doc['stars'],
                reviews=curr_doc['reviews'],
                price=curr_doc['price'],
                list_price=curr_doc['listPrice'],
                sub_category_id=curr_doc['sub_category_id'],
                sub_category_name=curr_doc['sub_category_name'],
                category_name=curr_doc['category_name'],
                is_best_seller=curr_doc['isBestSeller'],
                bought_in_last_month=curr_doc['boughtInLastMonth'],
                gender=curr_doc["gender"]
            )
            response = document.save(using=self.opensearch_client)
            logger.info(f'document successfully inserted with document id: {document_id}')
        except Exception as err:
            logger.error(f'Unable to insert a document with id {document_id}', error=err)
            logger.error("An exception occurred: %s", err)

    def get_document_by_id(self, document_id):
        search = self.search_client.filter("match", asin=document_id)
        result = search.execute()
        resp = []
        for hit in result:
            resp.append(to_dict(hit))
        return resp[0]

    def get_documents_by_title(self, key, size=20, from_=0, filters=None):
        search = self.search_client.query("match", title=key)
        if filters:
            if filters['gender']:
                search = search.filter("match", gender=filters['gender'])
            if filters['sort']:
                search = search.sort({"price": {"order": filters['sort']}})

        result = search.extra(size=size, from_=from_).execute()
        resp = []
        for hit in result:
            resp.append(to_dict(hit))
        return resp

    def get_all_categories(self):
        script = {
            "source": "doc['category.keyword'].value + '|' + doc['sub_category.keyword'].value",
            "lang": "painless"
        }

        distinct_values_aggregation = {
            "terms": {
                "script": script,
                "size": 10000
            }
        }

        self.search_client.aggs.bucket('distinct_combinations', 'terms',
                                       **distinct_values_aggregation)

        result = self.search_client.execute()

        distinct_combinations = [bucket.key.split('|') for bucket in
                                 result.aggs.distinct_combinations.buckets]

        return distinct_combinations

    def delete_document(self, document_id):
        response = self.opensearch_client.delete(
            index=self.index_name,
            id=document_id
        )

    def get_documents_by_category(self, sub_category, size=20, from_=0):
        search = self.search_client.query("match", sub_category=sub_category)

        result = search.extra(size=size, from_=from_).execute()
        resp = []
        for hit in result:
            resp.append(to_dict(hit))
        return resp
