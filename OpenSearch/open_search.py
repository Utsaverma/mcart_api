from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth, Document, Keyword, \
    Text
import boto3

host = 'search-mcart-opensearch-xrbublv5nalyzklgzu4cilhsq4.ap-south-1.es.amazonaws.com'
region = 'ap-south-1'

credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region)

client = OpenSearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)




def create_index(index_name):
    index_body = {
        'settings': {
            'index': {
                'number_of_shards': 1
            }
        }
    }
    response = client.indices.create(index=index_name, body=index_body)
    print(response)

create_index('mcart-products')

class Product(Document):
    title = Text(fields={'raw': Keyword()})
    director = Text()
    year = Text()

    class Index:
        name = 'mcart-products'

    def save(self, ** kwargs):
        return super(Product, self).save(** kwargs)

Product.init(using=client)
doc = Product(meta={'id': 1}, title='Moneyball', director='Bennett Miller', year='2011')
response = doc.save(using=client)

# movies = '{ "index" : { "_index" : "my-dsl-index", "_id" : "2" } } \n { "title" : "Interstellar", "director" : "Christopher Nolan", "year" : "2014"} \n { "create" : { "_index" : "my-dsl-index", "_id" : "3" } } \n { "title" : "Star Trek Beyond", "director" : "Justin Lin", "year" : "2015"} \n { "update" : {"_id" : "3", "_index" : "my-dsl-index" } } \n { "doc" : {"year" : "2016"} }'
#
# client.bulk(movies)