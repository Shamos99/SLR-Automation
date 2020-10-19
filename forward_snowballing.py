from scholarly import scholarly, ProxyGenerator
from fp.fp import FreeProxy
import json
from title_matchinng import get_similarity


def set_new_proxy():
    proxy = FreeProxy(rand=True, timeout=1).get()
    pg = ProxyGenerator()
    pg.SingleProxy(http=proxy, https=proxy)
    scholarly.use_proxy(pg)
    # if proxy_works:
    #     break
    return proxy


def get_papers_query_link(link):
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


def forward_snowballing(keyword, abstract_string="", target_score_abstract=30, target_score_title=45, levels=2, target_papers=50):
    level = 0
    counter = 1
    query = test_query_keyword(keyword)
    result_list = []
    # with open("result3.txt", "w+", encoding="utf-8") as result_file:
    # result_file.write(f"level= {level}")
    # result_file.write("\n\n")
    # result_file.write('{"data":[')
    citation_scholar_links = []
    for q in query:
        score = get_similarity(keyword, q.bib["title"])
        if len(abstract_string) != 0:
            score_abstract = get_similarity(abstract_string, q.bib["abstract"])
        else:
            score_abstract = 100
        if score >= target_score_title and score_abstract >= target_score_abstract:
            print("Paper number: " + str(counter) + "\t" "Score: " + str(score))
            if counter == target_papers:
                result_list.append(q.bib)
                return result_list
            # result_file.write(json.dumps(q.bib) + ',')
            result_list.append(q.bib)
            # test = result_list[-1].get["ENTRYTYPE"]
            counter += 1
        try:
            cite_link = q.citations_link
            citation_scholar_links.append(cite_link)
        except AttributeError as e:
            print(e)
            continue
    level += 1
    for _ in range(levels - 1):
        all_papers = get_papers_query_link(citation_scholar_links)
        citation_scholar_links = []
        for p in all_papers:
            for paper in p:
                score = get_similarity(keyword, paper.bib["title"])
                if len(abstract_string) != 0:
                    score_abstract = get_similarity(abstract_string, paper.bib["abstract"])
                else:
                    score_abstract = 100
                if score >= target_score_title and score_abstract >= target_score_abstract:
                    print("Paper number: " + str(counter) + "\t" "Score: " + str(score))
                    if counter == target_papers:
                        result_list.append(paper.bib)
                        return result_list
                    # result_file.write(json.dumps(paper.bib) + ',')
                    result_list.append(paper.bib)
                    counter += 1

                try:
                    cite_link = q.citations_link
                    citation_scholar_links.append(cite_link)
                except AttributeError as e:
                    print(e)
                    continue
        level += 1
        # result_file.close()


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
    #     # Currently set as Batarang cause the scholarly blocks us for insane number of requests...
    #     s = test_query_keyword("modernizing the systematic review pipeline")
    #     print(s)
    # lol = next(s)
    # print(lol)
    # print(json.dumps(lol.bib))
    ans = forward_snowballing("modernizing the systematic review pipeline", target_papers=20)
    print(ans)
    # test_query_keyword(
    #     "Alternative to mental hospital treatment: I. Conceptual model, treatment program, and clinical evaluation")
