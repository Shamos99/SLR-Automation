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


def get_title_results(title_string):
    url = "https://api.crossref.org/works?query="

    query_string = url + str(title_string)
    citation_json_obj = query_get_request(query_string)

    search_results = citation_json_obj["message"]["items"]
    for result in search_results:
        try:
            for title in result["title"]:
                if title.lower() in title_string.lower():
                    return result
        except KeyError as e:
            pass
    return None


if __name__ == '__main__':
    print(title_to_doi(
        "Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining"))
    pprint.pprint(get_title_results(
        "Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining"))
