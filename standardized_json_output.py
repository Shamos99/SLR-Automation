import datetime
import pprint
from query_api import get_title_results

api_enum = {
    "google_scholar": 0,
    "crossref": 1
}


def standarized_dict(dictionary, new_key, old_key):
    if old_key in dictionary:
        dictionary[new_key] = dictionary[old_key]
    else:
        dictionary[new_key] = None


def standardized_list(list_inpt, enum):
    if enum == 0:
        for entry in list_inpt:
            standarized_dict(entry, "publication_date", "year")
            entry["publication_date"] = datetime.datetime.strptime(str(entry["publication_date"])+ "-01","%Y-%m")
            standarized_dict(entry, "impact_factor", "N/A")
            standarized_dict(entry, "journal", "N/A")
            standarized_dict(entry, "h-index", "N/A")
            standarized_dict(entry, "publication_type", "N/A")
            standarized_dict(entry, "location", "N/A")
            standarized_dict(entry, "n_cited_by", "cites")
            standarized_dict(entry, "language", "N/A")

    elif enum == 1:
        for entry in list_inpt:
            standarized_dict(entry, "publication_date", "published-print")
            entry["publication_date"] = datetime.datetime.strptime(str(entry["publication_date"]["date-parts"][0][0]) + "-" + str(
                entry["publication_date"]["date-parts"][0][1]),"%Y-%m")
            standarized_dict(entry, "impact_factor", "N/A")
            standarized_dict(entry, "journal", "container-title")
            entry["journal"] = entry["journal"][0]
            standarized_dict(entry, "h-index", "N/A")
            standarized_dict(entry, "publication_type", "type")
            standarized_dict(entry, "location", "N/A")
            standarized_dict(entry, "n_cited_by", "is-referenced-by-count")
            standarized_dict(entry, "language", "language")


if __name__ == '__main__':
    result_dict = get_title_results(
        "Toward modernizing the systematic review pipeline in genetics: efficient updating via data mining")
    standardized_list([result_dict],
                      enum=api_enum["crossref"])
    pprint.pprint(result_dict)
