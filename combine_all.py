from stage2.standardized_json_output import standardized_list, api_enum
from stage2.fuck_u_in_the_ass import store_list_to_file
from stage3.inclusion_exclusion_criterion import apply_criterion
from stage3.criterion_params import criterion_param
from stage3.constants import *
from stage2.forward_snowballing import forward_snowballing
from stage2.backwards_snowball import backwards_snowballing_levels


class SLR_Automation:

    def __init__(self, search_string,
                 backward_snowballing_paper_string,
                 filter_list,
                 criterion_param,
                 true_abstract_list=[],
                 title_similarity_score=45,
                 abstract_similarity_score=45,
                 forward_snowballing_target=50,
                 forward_snowballing_levels=1,
                 backward_snowballing_levels=1,
                 backward_snowballing_target=10,
                 filename_to_store_result="result.txt"):
        self.search_string = search_string
        self.abstract_similarity_score = abstract_similarity_score
        self.title_similarity_score = title_similarity_score
        self.backward_snowballing_levels = backward_snowballing_levels
        self.forward_snowballing_levels = forward_snowballing_levels
        self.forward_snowballing_target_papers = forward_snowballing_target
        self.backward_snowballing_target_papers = backward_snowballing_target
        self.backward_snowballing_paper_string = backward_snowballing_paper_string
        self.true_abstract_string = ""
        self.forward_snowballing_results = []
        self.backward_snowballing_result = []
        self.filename_to_store_result = filename_to_store_result
        for i in true_abstract_list:
            self.search_string += i

        self.filter_list = filter_list
        self.criterion_param = criterion_param

    def perform_forward_snowballing(self):
        self.forward_snowballing_result = forward_snowballing(self.search_string,
                                                              self.true_abstract_string,
                                                              target_score_abstract=self.abstract_similarity_score,
                                                              target_papers=self.forward_snowballing_target_papers,
                                                              levels=self.forward_snowballing_levels,
                                                              target_score_title=self.title_similarity_score)

    def perform_backward_snowballing(self):
        print(self.backward_snowballing_target_papers)
        self.backward_snowballing_result = backwards_snowballing_levels(self.backward_snowballing_paper_string,
                                                                        self.search_string,
                                                                        level=self.backward_snowballing_levels,
                                                                        target_score_title=self.title_similarity_score,
                                                                        paper_target=self.backward_snowballing_target_papers
                                                                        )

    def combine_snowballing_results(self):
        standardized_list(self.forward_snowballing_result, api_enum["google_scholar"])
        backward_snowballing_standardised = standardized_list(self.backward_snowballing_result, api_enum["crossref"])
        self.final_results = self.forward_snowballing_result + self.backward_snowballing_result

    def perform_stage_two(self):
        self.perform_forward_snowballing()
        print("FINISHED FORWARD SNOWBALLING-----------------")
        self.perform_backward_snowballing()
        print("FINISHED BACKWARD SNOWBALLING----------------")
        self.combine_snowballing_results()
        return self.final_results

    def perform_filtering(self):
        self.final_results = apply_criterion(self.final_results, self.filter_list, self.criterion_param)
        return self.final_results

    def finalize_and_save_to_file(self):
        store_list_to_file(self.filename_to_store_result, self.final_results)

    def do_the_thing(self):
        self.perform_stage_two()
        self.perform_filtering()
        self.finalize_and_save_to_file()


if __name__ == '__main__':
    search = "software fault prediction & software metrics & metadata"
    paper = "Analyzing maintainability and reliability of object-oriented software using weighted complex network"

    test = SLR_Automation(
        search,
        paper,
        None,
        None,
        forward_snowballing_levels=2,
        backward_snowballing_levels=2,
        backward_snowballing_target=50,
        forward_snowballing_target=50,
        filename_to_store_result="Chong_test1"
    )

    test.perform_stage_two()
    test.finalize_and_save_to_file()

    # print("STAGE 2 -----------------------------------------------------")
    # print(test.perform_stage_two())
    # print("-------------------------------------------------------------")
    # param_dict = criterion_param
    # param_dict[YEAR][min_year] = '2012-07-01 00:00:00'
    # param_dict[YEAR][max_year] = '2020-07-01 00:00:00'
    #
    # param_dict[N_CITED_BY][min_cited_by] = 5
    # param_dict[N_CITED_BY][max_cited_by] = 1000
    # filter_list = [
    #     YEAR,
    #     N_CITED_BY
    #     # IMPACT_FACTOR
    #     # JOURNAL
    #     # H_INDEX
    #     # PUBLICATION_TYPE
    #     # LOCATION
    #     # LANGUAGE
    # ]
    # print("STAGE 2 -----------------------------------------------------")
    # print(test.perform_filtering(filter_list, param_dict))
    # print("-------------------------------------------------------------")
    # test.finalize_and_save_to_file()
