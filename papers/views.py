import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils.date_utils import convert_date_to_es_format
from search import settings

from .constants import SEARCH_URL
from elasticsearch import Elasticsearch


class FetchPapersView(APIView):

    def get(self, request, **kwargs):

        # Fetching query params and preparing request data
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        start_date = convert_date_to_es_format(start_date)
        end_date = convert_date_to_es_format(end_date)
        query = {
            "query": {
                "range": {
                    "created": {
                    "gte": start_date,
                    "lte": end_date,
                    "format": "yyyy-MM-dd"
                    }
                }
            }
        }

        # Initializing ElasticSearch client
        es = Elasticsearch()
        # Sending out request to ElasticSearch server to return search results
        response = es.search(
            index=settings.ES_INDEX_NAME,
            body=query
        )

        return Response(response, status=status.HTTP_200_OK)
