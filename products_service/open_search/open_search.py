from opensearchpy import OpenSearch, RequestsHttpConnection


class OpenSearchClient:
    def __init__(self, host, auth):
        self.open_search_client = OpenSearch(
            hosts=[{'host': host, 'port': 443}],
            http_auth=auth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )

    def get_client(self):
        return self.open_search_client

    def create_index(self, index_name):
        index_body = {
            'settings': {
                'index': {
                    'number_of_shards': 1
                }
            }
        }
        self.open_search_client.indices.create(index=index_name, body=index_body, ignore=400)

    def delete_index(self, index_name):
        self.open_search_client.indices.delete(index=index_name, ignore=[400, 404])

