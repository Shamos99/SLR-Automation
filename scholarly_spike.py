from scholarly import scholarly
from scholarly import scholarly, ProxyGenerator
from fp.fp import FreeProxy



def set_new_proxy():
    proxy = FreeProxy(rand=True, timeout=1).get()
    pg = ProxyGenerator()
    pg.SingleProxy(http=proxy, https=proxy)
    scholarly.use_proxy(pg)
    # if proxy_works:
    #     break
    return proxy

def test_query_link(link):
    all_papers = []
    for i in link:
        search_query = search_pubs_url_with_proxy(i)
        all_papers.append(search_query)
    return all_papers

def search_pubs_url_with_proxy(url):
    try:
        search_query = scholarly.search_pubs_custom_url(url)
        return search_query
    except Exception as e:
        set_new_proxy()
        return search_pubs_url_with_proxy(url)


def forward_snowballing(query, levels=2):
    level = 0
    with open("result.txt", "w", encoding="utf-8") as result_file:
        result_file.write(f"level= {level}")
        result_file.write("\n\n")
        citation_scholar_links = []
        for q in query:
            result_file.write(str(q))
            result_file.write('\n\n')
            try:
                cite_link = q.citations_link
                citation_scholar_links.append(cite_link)
            except AttributeError as e:
                print(e)
                continue
        level += 1
        for _ in range(levels - 1):
            result_file.write(f"level= {level}")
            result_file.write("\n\n")
            all_papers = test_query_link(citation_scholar_links)
            citation_scholar_links = []
            for p in all_papers:
                for paper in p:
                    result_file.write(str(paper))
                    try:
                        cite_link = q.citations_link
                        citation_scholar_links.append(cite_link)
                    except AttributeError as e:
                        print(e)
                        continue
            level += 1
        result_file.close()


def test_query_keyword(keyword):
    try:
        search_query = scholarly.search_pubs(keyword)
        # print(next(search_query))
        return search_query
    except Exception as e:
        set_new_proxy()
        return test_query_keyword(keyword)
    # cite_link = next(search_query).citations_link
    # print(cite_link)
    # return cite_link


if __name__ == '__main__':
    # Currently set as Batarang cause the scholarly blocks us for insane number of requests...
    s = test_query_keyword("Batarang")
    forward_snowballing(s)
    # test_query_keyword(
    #     "Alternative to mental hospital treatment: I. Conceptual model, treatment program, and clinical evaluation")
