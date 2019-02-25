from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FetchPapersView(APIView):

    def get(self, *args, **kwargs):
        return Response("OK", status=status.HTTP_200_OK)