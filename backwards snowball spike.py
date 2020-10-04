import urllib3
import json
from query_api import query_get_request

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
    results = query_get_request(query_str)

    return results


if __name__ == '__main__':
    print(get_backward_citations("10.1038/gim.2012.7"))
    print(title_to_backwards_citations(
        "Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining"))

