from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core import queries as core_queries
from core.utils.date_utils import convert_date_to_es_format, get_today_date
from papers.utils import send_es_request


class FetchCategoryPapersView(APIView):
    """
    FetchCategoryPapersView
    """
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
        to = request.GET.get('to', None)
        till = request.GET.get('from', None)
        query = {}

        # Depending on the start/end date filters we convert them to ES time format
        if start_date:
            start_date = convert_date_to_es_format(start_date)
        if end_date:
            end_date = convert_date_to_es_format(end_date)

        # If filtering is based on the primary category
        if primary_category is not None:
            query = core_queries.get_primary_category_query
            query['query']['bool']['must'][0]['match']['primary_category'] = primary_category

        # If filtering is based on the secondary query
        elif category is not None:
            query = core_queries.get_sub_category_query
            query['query']['bool']['must'][0]['match']['categories'] = category

        # Based on the start and end dates we tweak our ES query
        if start_date and end_date:
            query['query']['bool']['filter'][0]['range']['created']['lte'] = end_date
            query['query']['bool']['filter'][0]['range']['created']['gte'] = start_date
        elif start_date and not end_date:
            query['query']['bool']['filter'][0]['range']['created']['gte'] = start_date
            query['query']['bool']['filter'][0]['range']['created'].pop('lte')
        query['from'] = to
        query['to'] = till
        response = send_es_request(query)
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
        query = core_queries.abstract_recent_query
        query['query']['match']['created'] = today
        response = send_es_request(query)

        return Response(response, status=status.HTTP_200_OK)


class UniversalSearch(APIView):

    def get(self, request, **kwargs):
        """
        This API is designed to return the simple Search results, it accepts a search query and that will be searched in all the fields.
        :param request:
        :param kwargs:
        :return:
        """
        # Forming filter today's papers query
        q = request.GET.get('query', None)
        to = request.GET.get('to', 0)
        till = request.GET.get('from', 10)
        query = core_queries.universal_search
        query['query']['multi_match']['query'] = q
        query['to'] = to
        query['from'] = till
        response = send_es_request(query)

        return Response(response, status=status.HTTP_200_OK)


class AdvancedSearch(APIView):

    def get(self, request, **kwargs):
        """
        This API is designed to return the Advanced Search results, it took only one query param at at a time.
        :param request:
        :param kwargs:
        :return:
        """
        # Forming filter today's papers query
        query = request.data.get('query', None)
        arxiv_id = request.data.get('arxiv_id', None)
        author = request.data.get('author', None)
        title = request.data.get('title', None)
        abstract = request.data.get('abstract', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        to = request.GET.get('to', None)
        till = request.GET.get('from', None)
        query = {}

        # Depending on the start/end date filters we convert them to ES time format
        if start_date:
            start_date = convert_date_to_es_format(start_date)
        if end_date:
            end_date = convert_date_to_es_format(end_date)

        # Search Query building
        query = core_queries.advance_search

        if arxiv_id is not None:
            query['query']['bool']['must'][0]['match']['arxiv_id'] = arxiv_id
        if author is not None:
            query['query']['bool']['must'][0]['match']['author'] = author
        if title is not None:
            query['query']['bool']['must'][0]['match']['title'] = title
        if abstract is not None:
            query['query']['bool']['must'][0]['match']['abstract'] = abstract
        query['to'] = to
        query['from'] = till

        response = send_es_request(query)

        return Response(response, status=status.HTTP_200_OK)
