from django.conf import settings
from elasticsearch import Elasticsearch

from core.utils.response_parser import es_request_parser


def send_es_request(query):
    """
    send_es_request
    :return:
    """
    # Initializing ElasticSearch client
    es = Elasticsearch()
    # Sending out request to ElasticSearch server to return search results
    response = es.search(
        index=settings.ES_INDEX_NAME,
        body=query
    )
    return es_request_parser(response)
