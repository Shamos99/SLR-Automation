from scholarly import scholarly


def get_abstract_from_title(title_string):
    """
    The name of the function is pretty obv
    """
    if type(title_string) != str:
        return None

    search_query = scholarly.search_pubs(title_string)
    try:
        search_result = next(search_query).bib
        if search_result['title'] == title_string:
            return search_result['abstract']
        raise Exception
    except Exception:
        return None


if __name__ == '__main__':
    print(get_abstract_from_title(
        "Alternative to mental hospital treatment: I. Conceptual model, treatment program, and clinical evaluation"))
