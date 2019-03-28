import json
import logging
from datetime import datetime
from pprint import pprint

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from papers.constants import DB_STRUCTURE

logger = logging.getLogger(__name__)


def validate_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        print("Invalid json:")
        pprint(data)
        return False


def dump_json_to_elasticsearchdb():

    ACCEPTABLE_ERROR_CODES = ["200", "201"]

    # Defining server consts
    ES_FIELD_LIMIT = settings.ES_FIELD_LIMIT
    ES_SERVER_URL = settings.ES_SERVER_URL
    ES_INDEX_NAME = settings.ES_INDEX_NAME
    ES_DOCUMENT_TYPE = settings.ES_DOCUMENT_TYPE

    # Create an ES index
    index_url = ES_SERVER_URL + ES_INDEX_NAME
    logger.info("ES Index URL: {}".format(index_url))
    requests.put(url=index_url, data=DB_STRUCTURE)

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

    # Open file
    with open('data.json') as f:
        data = json.load(f)

    # Load data sequentially
    for key, value in data.items():

        paper = {}
        paper[key] = value
        # paper = json.dumps(paper)
        # import pdb; pdb.set_trace()
        datetime.strptime(paper['6220']['created'], "%Y-%m-%d %H:%M:%S")
        paper['created'] = datetime.strptime(paper['created'], "%Y-%m-%d %H:%M:%S.%f")
        if validate_json(paper):
            requests.post(
                url=load_data_url,
                data=paper,
                headers=headers
            )

    if str(response.status_code) not in ACCEPTABLE_ERROR_CODES:
        logger.info("Uh Oh! Ran into a data upload error :/ ")


class Command(BaseCommand):
    def handle(self, *args, **options):
        dump_json_to_elasticsearchdb()
