import json


def es_request_parser(response):
    response = response["hits"]["hits"]
    parsed_response = []
    for i in response:
        parsed_response.append(i["_source"])
    return parsed_response
