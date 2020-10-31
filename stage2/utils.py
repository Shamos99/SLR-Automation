import urllib3
import json


def query_get_request(query_string):
    """
    Does a request with a query string
    :param query_string: query string for request
    :return: json dict
    """
    http = urllib3.PoolManager()
    request = http.request("GET", query_string)
    return json.loads(request.data.decode())
