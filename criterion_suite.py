import criterion_params as params


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

        ans_list = []


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
            if min_factor < paper['impact_factor'] < max_factor:
                ans_list.append(1)
            else:
                ans_list.append(0)

        return ans_list


class JournalFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):
        journal_list = param[params.journal_list]


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
            if min_index < paper['impact_factor'] < max_index:
                ans_list.append(1)
            else:
                ans_list.append(0)

        return ans_list


class PublicationTypeFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):
        pub_type_list = param[params.publication_types_list]


class LocationFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):
        location_list = param[params.location_list]


class NCitedByFilter(GenericFilter):

    @staticmethod
    def impl(pub_list, param):
        min_cited_by = param[params.min_cited_by]
        max_cited_by = param[params.max_cited_by]

        ans_list = [0] * len(pub_list)

        if min_cited_by is None and max_cited_by is None:
            return ans_list

        if min_cited_by is None:
            min_cited_by = float('-inf')

        if max_cited_by is None:
            max_cited_by = float('inf')

        for paper in pub_list:
            if min_cited_by < paper['impact_factor'] < max_cited_by:
                ans_list.append(1)
            else:
                ans_list.append(0)

        return ans_list


if __name__ == '__main__':
    pass
