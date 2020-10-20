import criterion_params as params
from datetime import datetime
import constants


# all of the inclusion exclusion criterion we have will be in this file


class GenericFilter:

    @staticmethod
    def impl(pub_list, param):
        pass


class YearFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):

        min_year = param[params.min_year]
        max_year = param[params.max_year]

        if min_year is None:
            min_year = datetime.strptime(constants.MIN_DATE, constants.DATE_FORMAT)
        else:
            min_year = datetime.strptime(param[params.min_year], constants.DATE_FORMAT)

        if max_year is None:
            max_year = datetime.strptime(constants.MAX_DATE, constants.DATE_FORMAT)
        else:
            max_year = datetime.strptime(param[params.max_year], constants.DATE_FORMAT)

        ans_list = []

        for i in range(len(pub_list)):

            if "publication_date" not in pub_list[i] or pub_list[i]["publication_date"] == 'null':
                ans_list.append(1)
                continue

            this_date = datetime.strptime(pub_list[i]["publication_date"], constants.DATE_FORMAT)
            if min_year < this_date < max_year:
                ans_list.append(1)
            else:
                ans_list.append(0)

        return ans_list


class ImpactFactorFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):
        min_factor = param[params.min_impact]
        max_factor = param[params.max_impact]

        ans_list = [0] * len(pub_list)

        if min_factor is None and max_factor is None:
            return ans_list

        if min_factor is None:
            min_factor = float('-inf')

        if max_factor is None:
            max_factor = float('inf')

        for paper in pub_list:

            if 'impact_factor' not in param:
                ans_list.append(1)
                continue

            if min_factor < paper['impact_factor'] < max_factor:
                ans_list.append(1)
            else:
                ans_list.append(0)

        return ans_list


class JournalFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):
        journal_list = param[params.journal_list]

        res = []

        # naiive code
        for paper in pub_list:
            for journal in journal_list:
                if journal in paper['journal_list']:
                    res.append(1)
            res.append(0)

        return res


class HIndexFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):
        min_index = param[params.min_h_index]
        max_index = param[params.max_h_index]

        ans_list = [0] * len(pub_list)

        if min_index is None and max_index is None:
            return ans_list

        if min_index is None:
            min_index = float('-inf')

        if max_index is None:
            max_index = float('inf')

        for paper in pub_list:

            if 'impact_factor' not in paper:
                ans_list.append(1)

            if min_index < paper['impact_factor'] < max_index:
                ans_list.append(1)
            else:
                ans_list.append(0)

        return ans_list


class PublicationTypeFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):
        pub_type_list = param[params.publication_types_list]

        res = []

        # naiive code
        for paper in pub_list:
            for pub in pub_type_list:
                if pub in paper['publication_list']:
                    res.append(1)
            res.append(0)

        return res


class LocationFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):
        location_list = param[params.location_list]

        res = []

        # naiive code
        for paper in pub_list:
            for loc in location_list:
                if loc in paper['location_list']:
                    res.append(1)
            res.append(0)

        return res


class NCitedByFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):
        min_cited_by = param[params.min_cited_by]
        max_cited_by = param[params.max_cited_by]

        ans_list = []

        if min_cited_by is None and max_cited_by is None:
            return ans_list

        if min_cited_by is None:
            min_cited_by = float('-inf')

        if max_cited_by is None:
            max_cited_by = float('inf')

        for paper in pub_list:

            if 'n_cited_by' not in paper:
                ans_list.append(1)
                continue

            if min_cited_by < paper['n_cited_by'] < max_cited_by:
                ans_list.append(1)
            else:
                ans_list.append(0)

        return ans_list


class LanguageFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):
        language = param[params.language]

        res = []

        for pub in pub_list:
            if pub['language'] == language:
                res.append(1)
            else:
                res.append(0)

        return res


if __name__ == '__main__':
    pass
