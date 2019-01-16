import requests
import logging
from search.settings import ES_SERVER_URL, ES_INDEX_NAME, ES_DOCUMENT_TYPE, ES_FIELD_LIMIT
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

def dump_json_to_elasticsearchdb():
    ACCEPTABLE_ERROR_CODES = ["200", "201"]
    
    # Create an ES index
    index_url = ES_SERVER_URL + ES_INDEX_NAME
    logger.info("ES Index URL: {}".format(index_url))
    requests.put(index_url)

    # Increase field upload count to accommodate our json data
    headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}

    field_count_url = ES_SERVER_URL + ES_INDEX_NAME + '/_settings'
    logger.info("ES Field Count Update URL: {}".format(field_count_url))

    response = requests.put(
        url=field_count_url,
        json={
            "index.mapping.total_fields.limit": ES_FIELD_LIMIT
        },
        headers=headers
    )
    if str(response.status_code) not in ACCEPTABLE_ERROR_CODES:
        logger.info("Uh oh! Ran into a field update error :/ ")

    # Send data to ES server
    load_data_url = ES_SERVER_URL + ES_INDEX_NAME + "/" + ES_DOCUMENT_TYPE
    logger.info("ES Data Load URL: {}".format(load_data_url))

    requests.post(
        url=load_data_url,
        data=open('data.json', 'rb'),
        headers=headers
    )

    if str(response.status_code) not in ACCEPTABLE_ERROR_CODES:
        logger.info("Uh Oh! Ran into a data upload error :/ ")

class Command(BaseCommand):
    def handle(self, *args, **options):
        dump_json_to_elasticsearchdb()