import gscholar
from scholarly import scholarly

def test_query_link(link):
    search_query = scholarly.search_pubs_custom_url(link)
    print("-- Cite --")
    print(next(search_query))

def test_query_keyword(keyword):
    search_query = scholarly.search_pubs(keyword)
    # for q in search_query:
    #     print(q)
    cite_link = next(search_query).citations_link
    print(cite_link)
    return cite_link


if __name__ == '__main__':
    c = test_query_keyword("testing")
    test_query_link(c)