from scholarly import scholarly


def test_query_link(link):
    all_papers = []
    for i in link:
        search_query = scholarly.search_pubs_custom_url(i)
        all_papers.append(search_query)
    return all_papers


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
    search_query = scholarly.search_pubs(keyword)
    print(next(search_query))
    return search_query
    # cite_link = next(search_query).citations_link
    # print(cite_link)
    # return cite_link


if __name__ == '__main__':
    # Currently set as Batarang cause the scholarly blocks us for insane number of requests...
    # s = test_query_keyword("Batarang")
    # foward_snowballing(s)
    test_query_keyword(
        "Alternative to mental hospital treatment: I. Conceptual model, treatment program, and clinical evaluation")
