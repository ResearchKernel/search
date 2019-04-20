from elasticsearch import Elasticsearch
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core import queries as core_queries
from core.utils.date_utils import convert_date_to_es_format, get_today_date
from search import settings


class FetchPapersView(APIView):

    def get(self, request, **kwargs):
        """
            The API is designed to perform filtered query on ElasticSearch
        :param request:
        :param kwargs:
        :return:
        """

        # Fetching query params and preparing request data
        primary_category = request.data.get('primary_category', None)
        category = request.data.get('category', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        query = {}

        # Depending on the start/end date filters we convert them to ES time format
        if start_date:
            start_date = convert_date_to_es_format(start_date)
        if end_date:
            end_date = convert_date_to_es_format(end_date)

        # If filtering is based on the primary category
        if primary_category is not None:
            query = core_queries.primary_category_query
            query['query']['bool']['must'][0]['match']['primary_category'] = primary_category

        # If filtering is based on the secondary query
        elif category is not None:
            query = core_queries.category_query
            query['query']['bool']['must'][0]['match']['categories'] = category

        # Based on the start and end dates we tweak our ES query
        if start_date and end_date:
            query['query']['bool']['filter'][0]['range']['created']['lte'] = start_date
            query['query']['bool']['filter'][0]['range']['created']['gte'] = end_date
        elif start_date and not end_date:
            query['query']['bool']['filter'][0]['range']['created']['lte'] = start_date
            query['query']['bool']['filter'][0]['range']['created'].pop('gte')

        # Initializing ElasticSearch client
        es = Elasticsearch()
        # Sending out request to ElasticSearch server to return search results
        response = es.search(
            index=settings.ES_INDEX_NAME,
            body=query,
        )

        return Response(response, status=status.HTTP_200_OK)


class RecentPaperView(APIView):

    def get(self, request, **kwargs):
        """
            This API is designed to return the recent papers
        :param request:
        :param kwargs:
        :return:
        """
        # Forming filter today's papers query
        today = get_today_date()
        query = core_queries.recent_query
        query['query']['match']['created'] = today

        # Initializing ElasticSearch client
        es = Elasticsearch()
        # Sending out request to ElasticSearch server to return search results
        response = es.search(
            index=settings.ES_INDEX_NAME,
            body=query
        )

        return Response(response, status=status.HTTP_200_OK)
