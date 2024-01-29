import logging
import os

import boto3
import pandas as pd
from opensearchpy import AWSV4SignerAuth

from .open_search import OpenSearchClient
from .document_operations import DocumentOperations

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_document_util():
    host_name = os.environ['HOST']
    region = os.environ['REGION']

    credentials = boto3.Session().get_credentials()
    auth = AWSV4SignerAuth(credentials, region)

    opensearch_obj = OpenSearchClient(host_name, auth)
    opensearch_client = opensearch_obj.get_client()
    index_name = get_index_name()
    documents_util = DocumentOperations(opensearch_client, index_name)

    # opensearch_obj.create_index(index_name)

    # try:
    #     bulk_insert(opensearch_client)
    #     logger.info('All documents inserted')
    # except Exception as err:
    #     logger.error("An exception occurred: %s", err)

    # documents_util.get_document_by_id('B0C4RMF5PZ')
    # documents_util.get_documents_by_title('T-Shirt')
    return documents_util

def bulk_insert(opensearch_client):
    document_list = get_all_data()
    chunk_size = 4000
    total_inserted = 205000
    for i in range(205000, len(document_list), chunk_size):
        chunk = document_list[i:i + chunk_size]
        curr_query = process_chunk(chunk)
        total_inserted = total_inserted + chunk_size
        opensearch_client.bulk(curr_query)
        print(total_inserted)


def process_chunk(chunk):
    list = []
    for curr_doc in chunk:
        list.append({"create": {"_index": get_index_name(), "_id": str(curr_doc['asin'])}})
        list.append(curr_doc)
    return list


def get_index_name():
    return 'mcart-products'


def get_all_data():
    df = pd.read_csv(r'mcart_products_act.csv', sep=",")
    return df.to_dict(orient='records')


if __name__ == "__main__":
    get_document_util()
    # get_all_data()
    pass