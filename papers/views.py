import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils.date_utils import convert_date_to_es_format, get_today_date
from elasticsearch import Elasticsearch
from search import settings

from .constants import SEARCH_URL


class FetchPapersView(APIView):

    def get(self, request, **kwargs):

        # Fetching query params and preparing request data
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        if start_date:
            start_date = convert_date_to_es_format(start_date)
        if end_date:
            end_date = convert_date_to_es_format(end_date)

        if start_date and end_date:
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
        elif start_date and not end_date:
            query = {
                "query": {
                    "match" : {
                        "created" : start_date
                    }
                }
            }
        else:
            query = {}

        # Initializing ElasticSearch client
        es = Elasticsearch()
        # Sending out request to ElasticSearch server to return search results
        response = es.search(
            index=settings.ES_INDEX_NAME,
            body=query
        )

        return Response(response, status=status.HTTP_200_OK)


class RecentPaperView(APIView):

    def get(self, request, **kwargs):

        today = get_today_date()
        query = {
            "query": {
                "match": {
                    "created": today
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
