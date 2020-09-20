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


def title_to_backwards_citations(title_string):
    """
    getting refernce list of title from a title string
    :param title_string: a title string for a paper
    :return: reference list
    """

    url = "https://api.crossref.org/works?query="

    query_string = url + str(title_string)
    citation_json_obj = query_get_request(query_string)

    search_results = citation_json_obj["message"]["items"]
    for result in search_results:
        for title in result["title"]:
            if title == title_string:
                return result["reference"]
    return None


def title_to_doi(title_string):
    """

    :param title_string:
    :return:
    """

    url = "https://api.crossref.org/works?query="
    query_string = url + str(title_string)

    citation_json_obj = query_get_request(query_string)
    search_results = citation_json_obj["message"]["items"]
    for result in search_results:
        for title in result["title"]:
            if title == title_string:
                return result["DOI"]
    return None


def get_backward_citations(doi):
    """
    Gets backwards snowballed citations as a json object
    :param doi: doi of paper to retrieve citations
    :return: json object with papers cited by given doi
    """

    # request url
    url = "https://opencitations.net/index/api/v1/references/"

    # query string
    query_str = url + str(doi)
    request = query_get_request(query_str)

    return json.loads(request.data.decode())


if __name__ == '__main__':
    print(get_backward_citations("10.1007/s10434-001-0204-4"))
    print(title_to_backwards_citations(
        "Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining"))
    print(title_to_doi(
        "Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining"))
