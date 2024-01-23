import os

import boto3
from opensearchpy import AWSV4SignerAuth
from products_service.open_search.open_search import OpenSearchClient
from products_service.open_search.document_operations import DocumentOperations
from products_service.open_search.util import get_index_name


def search_by_title(title):
    if title:
        host_name = os.environ['HOST']
        region = os.environ['REGION']

        credentials = boto3.Session().get_credentials()
        auth = AWSV4SignerAuth(credentials, region)

        opensearch_obj = OpenSearchClient(host_name, auth)
        opensearch_client = opensearch_obj.get_client()
        index_name = get_index_name()
        documents_util = DocumentOperations(opensearch_client, index_name)

        items = documents_util.get_documents_by_title(title)
        return items


def search_by_id(id):
    if id:
        host_name = os.environ['HOST']
        region = os.environ['REGION']

        credentials = boto3.Session().get_credentials()
        auth = AWSV4SignerAuth(credentials, region)

        opensearch_obj = OpenSearchClient(host_name, auth)
        opensearch_client = opensearch_obj.get_client()
        index_name = get_index_name()
        documents_util = DocumentOperations(opensearch_client, index_name)

        return documents_util.get_document_by_id(id)