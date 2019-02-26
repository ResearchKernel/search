from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FetchPapersView(APIView):

    def get(self, request, **kwargs):

        start_date = request.GET.get('start_date')
        end_date = request.GET.get('start_date')

        
        return Response("OK", status=status.HTTP_200_OK)