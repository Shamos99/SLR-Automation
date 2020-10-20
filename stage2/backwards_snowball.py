import urllib3
import json
# from query_api import query_get_request
from stage2.title_matchinng import get_similarity, query_get_request


def title_to_backwards_citations(title_string, original_title, target_score_title=45):
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
            # print(title_string.lower())
            # print(title.lower())
            similarity_title = get_similarity(original_title.lower(), title.lower())
            # print(similarity)
            if (title.lower() in title_string.lower()) and (similarity_title >= target_score_title):
                try:
                    return result["reference"], result
                except Exception:
                    return None, None
    return None, None


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


def backwards_snowballing_levels(title_string, level=2, target_score_title=45):
    backwards,result = title_to_backwards_citations(title_string, title_string)
    full_list = [backwards]
    result_list = [result]

    level = level - 1
    counter = 0
    while level >= 0:
        # print(full_list)

        for title in full_list[counter]:
            try:
                check_title = title["unstructured"]
                append_item,result_item = title_to_backwards_citations(check_title, title_string, target_score_title)
                if append_item is not None:
                    full_list.append(append_item)
                if result_item is not None:
                    result_list.append(result_item)
            except Exception:
                pass

        counter += 1
        level = level - 1

    return result_list


if __name__ == '__main__':
    #     # print(get_backward_citations("10.1038/gim.2012.7"))
    #     # print(title_to_backwards_citations(
    #     #     "Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining"))
    #
    print(backwards_snowballing_levels("Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining", level=1))
