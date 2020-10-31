import urllib3
import json
import pprint


def query_get_request(query_string):
    """
    Does a request with a query string
    :param query_string: query string for request
    :return: json dict
    """
    http = urllib3.PoolManager()
    request = http.request("GET", query_string)
    return json.loads(request.data.decode())


def get_similarity(title1, title2):
    TOKEN = "515890c2d4e5419385013367e40fc5ac"
    query = "https://api.dandelion.eu/datatxt/sim/v1/?text1=" + str(title1) + "&text2=" + str(title2) + "&bow=one_empty" + "&token=" + TOKEN
    result = query_get_request(query)
    return result["similarity"] * 100


if __name__ == '__main__':
    # print(query_get_request(
    # "https://api.dandelion.eu/datatxt/sim/v1/?text1=Cameron%20wins%20the%20Oscar &text2=All%20nominees%20for%20the%20Academy%20Awards&token=515890c2d4e5419385013367e40fc5ac"))
    print(get_similarity("systematic literature review automation", "Impediments for software test automation: A systematic literature review"))
