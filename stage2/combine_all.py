from forward_snowballing import forward_snowballing
from backwards_snowball import backwards_snowballing_levels
from standardized_json_output import standardized_list, api_enum


class SLR_Automation:
    true_abstract_list = []
    search_string = ""
    true_abstract_string = ""
    title_similarity_score = 45
    abstract_similarity_score = 45
    forward_snowballing_target_papers = 50
    forward_snowballing_levels = 2
    forward_snowballing_results = []
    backward_snowballing_levels = 2
    backward_snowballing_result = []
    backward_snowballing_paper_string = ""
    final_resuls = []

    def __init__(self, true_abstract_list, search_string,
                 backward_snowballing_paper_string,
                 title_similarity_score=45,
                 abstract_similarity_score=45,
                 forward_snowballing_target=50,
                 forward_snowballing_levels=2,
                 backward_snowballing_levels=2):
        self.search_string = search_string
        self.abstract_similarity_score = abstract_similarity_score
        self.title_similarity_score = title_similarity_score
        self.backward_snowballing_levels = backward_snowballing_levels
        self.forward_snowballing_levels = forward_snowballing_levels
        self.forward_snowballing_target_papers = forward_snowballing_target
        self.backward_snowballing_paper_string = backward_snowballing_paper_string
        self.true_abstract_string = ""
        self.forward_snowballing_results = []
        self.backward_snowballing_result = []
        for i in true_abstract_list:
            self.search_string += i

    def perform_forward_snowballing(self):
        self.forward_snowballing_result = forward_snowballing(self.search_string,
                                                              self.true_abstract_string,
                                                              target_score_abstract=self.abstract_similarity_score,
                                                              target_papers=self.forward_snowballing_target_papers,
                                                              levels=self.forward_snowballing_levels,
                                                              target_score_title=self.title_similarity_score)

    def perform_backward_snowballing(self):
        self.backward_snowballing_result = backwards_snowballing_levels(self.backward_snowballing_paper_string,
                                                                        level=self.backward_snowballing_levels,
                                                                        target_score_title=self.title_similarity_score)

    def combine_snowballing_results(self):
        standardized_list(self.forward_snowballing_results, api_enum["google_scholar"])
        backward_snowballing_standardised = standardized_list(self.backward_snowballing_result, api_enum["crossref"])
        self.final_resuls = self.forward_snowballing_results + self.backward_snowballing_result

    def perform_stage_two(self):
        self.perform_forward_snowballing()
        self.perform_backward_snowballing()
        self.combine_snowballing_results()
        return self.final_resuls
