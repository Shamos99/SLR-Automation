import urllib3
import json
from query_api import query_get_request
from title_matchinng_spike import get_similarity


def title_to_backwards_citations(title_string,original_title ,target_score = 50):
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
            print(title_string.lower())
            print(title.lower())
            similarity = get_similarity(original_title.lower(), title.lower())
            print(similarity)
            if (title.lower() in title_string.lower()) and ( similarity >= target_score):
                try:
                    return result["reference"]
                except Exception:
                    return None
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

def backwards_snowballing_levels(title_string,level=2):

    full_list = [title_to_backwards_citations(title_string,title_string)]
    level = level -1
    counter = 0
    while level >= 0:
        print(full_list)

        for title in full_list[counter]:
            try:
                check_title = title["unstructured"]
                append_item = title_to_backwards_citations(check_title,title_string)
                if append_item is not None:
                    full_list.append(append_item)
            except Exception:
                pass

        counter += 1
        level = level-1
    return full_list

if __name__ == '__main__':
    # print(get_backward_citations("10.1038/gim.2012.7"))
    # print(title_to_backwards_citations(
    #     "Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining"))

    print(backwards_snowballing_levels("Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining"))

