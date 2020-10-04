import criterion_suite as suite
from criterion_params import criterion_param
from constants import *


def apply_criterion(publication_list, filter_list, param_dict):
    # loop and apply filters
    for filter_criteria in filter_list:

        if filter_criteria == YEAR:
            suite.YearFilter.impl(publication_list, param_dict[YEAR])

        elif filter_criteria == IMPACT_FACTOR:
            suite.ImpactFactorFilter.impl(publication_list, param_dict[IMPACT_FACTOR])

        elif filter_criteria == JOURNAL:
            suite.JournalFilter.impl(publication_list, param_dict[JOURNAL])

        elif filter_criteria == H_INDEX:
            suite.HIndexFilter.impl(publication_list, param_dict[H_INDEX])

        elif filter_criteria == PUBLICATION_TYPE:
            suite.PublicationTypeFilter.impl(publication_list, param_dict[PUBLICATION_TYPE])

        elif filter_criteria == LOCATION:
            suite.LocationFilter.impl(publication_list, param_dict[LOCATION])

        elif filter_criteria == N_CITED_BY:
            suite.NCitedByFilter.impl(publication_list, param_dict[N_CITED_BY])


if __name__ == '__main__':
    pass
