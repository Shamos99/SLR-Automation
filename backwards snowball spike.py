import urllib3
import json

def get_backward_citations(doi):
    """
    Gets backwards snowballed citations as a json object
    :param doi: doi of paper to retrieve citations
    :return: json object with papers cited by given doi
    """

    http = urllib3.PoolManager()

    # request url
    url = "https://opencitations.net/index/api/v1/references/"

    # query string
    query_str = url+str(doi)
    request = http.request("GET",query_str)

    return json.loads(request.data.decode())

if __name__ == '__main__':

    get_backward_citations("10.1007/s10434-001-0204-4")