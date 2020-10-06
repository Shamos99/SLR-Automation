import datetime
import pprint
import json
from query_api import get_title_results
from backwards_snowball_spike import title_to_backwards_citations

api_enum = {
    "google_scholar": 0,
    "crossref": 1
}


def standarized_dict(dictionary, new_key, old_key):
    if new_key == "publication_date":
        date_keys = ["indexed","published-print","published-online"]
        for date_key in date_keys:
            if date_key in dictionary:
                dictionary[new_key] = dictionary[date_key]
                break
        dictionary[new_key] = "-"
    else:
        if old_key in dictionary:
            dictionary[new_key] = dictionary[old_key]
        else:
            dictionary[new_key] = None


def standardized_list(list_inpt, enum):
    print(list_inpt)
    if enum == 0:
        for entry in list_inpt:
            if entry is None:
                continue
            standarized_dict(entry, "publication_date", "year")
            entry["publication_date"] = str(datetime.datetime.strptime(str(entry["publication_date"]) + "-01", "%Y-%m"))
            standarized_dict(entry, "impact_factor", None)
            standarized_dict(entry, "journal", None)
            standarized_dict(entry, "h-index", None)
            standarized_dict(entry, "publication_type", None)
            standarized_dict(entry, "location", None)
            standarized_dict(entry, "n_cited_by", "cites")
            standarized_dict(entry, "language", None)

    elif enum == 1:
        for entry in list_inpt:
            if entry is None:
                continue
            standarized_dict(entry, "publication_date", "published-print")
            if "date-parts" in entry["publication_date"]:
                entry["publication_date"] = str(datetime.datetime.strptime(
                    str(entry["publication_date"]["date-parts"][0][0]) + "-" + str(
                        entry["publication_date"]["date-parts"][0][1]), "%Y-%m"))
            else:
                entry["publication_date"] = None

            standarized_dict(entry, "impact_factor", None)
            standarized_dict(entry, "journal", "container-title")
            entry["journal"] = entry["journal"][0]
            standarized_dict(entry, "h-index", None)
            standarized_dict(entry, "publication_type", "type")
            standarized_dict(entry, "location", None)
            standarized_dict(entry, "n_cited_by", "is-referenced-by-count")
            standarized_dict(entry, "language", "language")


if __name__ == '__main__':
    backwards_citations = title_to_backwards_citations(
        "Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining")
    fin_list = []
    backwards_citations.append(get_title_results("Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining"))
    print("backwards finished")
    count = 0
    for result in backwards_citations:
        print("iteration ",count)
        try:
            result_dict = get_title_results(
                    result["unstructured"])
        except Exception as e:
            result_dict = {}
            pass

        fin_list.append(result_dict)
        count+=1
        if count == 15:
            break

    standardized_list(fin_list,
                      enum=api_enum["crossref"])
    print(fin_list)
    with open("stage2_output.json",'w') as f:
        json.dump(fin_list,f)

