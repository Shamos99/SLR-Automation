import criterion_suite as suite
import json
import pprint
from constants import *
from criterion_params import criterion_param


def resolve_result(on_going_arr, new_res):
    for i in range(len(on_going_arr)):
        if not new_res[i]:
            on_going_arr[i] = new_res[i]


def apply_criterion(publication_list, filter_list, param_dict):
    # loop and apply filters

    to_keep_arr = [1] * len(publication_list)

    for filter_criteria in filter_list:

        if filter_criteria == YEAR:
            res = suite.YearFilter.impl(publication_list, param_dict[YEAR])
            resolve_result(to_keep_arr, res)

        elif filter_criteria == IMPACT_FACTOR:
            res = suite.ImpactFactorFilter.impl(publication_list, param_dict[IMPACT_FACTOR])
            resolve_result(to_keep_arr, res)

        elif filter_criteria == JOURNAL:
            res = suite.JournalFilter.impl(publication_list, param_dict[JOURNAL])
            resolve_result(to_keep_arr, res)

        elif filter_criteria == H_INDEX:
            res = suite.HIndexFilter.impl(publication_list, param_dict[H_INDEX])
            resolve_result(to_keep_arr, res)

        elif filter_criteria == PUBLICATION_TYPE:
            res = suite.PublicationTypeFilter.impl(publication_list, param_dict[PUBLICATION_TYPE])
            resolve_result(to_keep_arr, res)

        elif filter_criteria == LOCATION:
            res = suite.LocationFilter.impl(publication_list, param_dict[LOCATION])
            resolve_result(to_keep_arr, res)

        elif filter_criteria == N_CITED_BY:
            res = suite.NCitedByFilter.impl(publication_list, param_dict[N_CITED_BY])
            resolve_result(to_keep_arr, res)

    final_pub_list = []

    for i in range(len(publication_list)):
        if to_keep_arr[i]:
            final_pub_list.append(publication_list[i])

    return final_pub_list


if __name__ == '__main__':
    filter_list = [
        #YEAR,
        N_CITED_BY
    ]

    param_dict = criterion_param

    param_dict[YEAR][min_year] = '2012-07-01 00:00:00'
    param_dict[YEAR][max_year] = '2020-07-01 00:00:00'

    param_dict[N_CITED_BY][min_cited_by] = 5
    param_dict[N_CITED_BY][max_cited_by] = 1000

    with open("stage2_output.json") as f:
        loaded = json.load(f)

    list = [x for x in loaded if x is not None]

    final = apply_criterion(list, filter_list, param_dict)

    print(len(final))
    pprint.pprint(final)
