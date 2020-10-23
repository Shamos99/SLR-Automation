from django.views.generic import CreateView
from django.template import loader
from .models import Slrform
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SLRForm
from bootstrap_datepicker_plus import DatePickerInput
from .combine_all import SLR_Automation
from .stage3 import constants
from .stage3.criterion_params import criterion_param


def slr_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SLRForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            is_error = False
            error_message = ""

            search_query = request.POST["search_query"]
            backward_snowballing_paper_string = request.POST['backward_snowballing_paper_string']
            title_similarity_score = request.POST['title_similarity_score']
            abstract_similarity_score = request.POST['abstract_similarity_score']
            forward_snowballing_target = request.POST['forward_snowballing_target']
            forward_snowballing_levels = request.POST['forward_snowballing_levels']
            backward_snowballing_levels = request.POST['backward_snowballing_levels']
            filename_to_store_result = request.POST['filename_to_store_result']

            year_min = request.POST['year_min'] if request.POST['year_min'] != "" else None
            year_max = request.POST['year_max'] if request.POST['year_max'] != "" else None
            min_impact_factor = request.POST['min_impact_factor'] if request.POST['min_impact_factor'] != "" else None
            max_impact_factor = request.POST['max_impact_factor'] if request.POST['max_impact_factor'] != "" else None
            journal_list = request.POST["journal_list"] if request.POST["journal_list"] != "" else None
            min_h_index = request.POST["min_h_index"] if request.POST["min_h_index"] != "" else None
            max_h_index = request.POST["max_h_index"] if request.POST["max_h_index"] != "" else None
            publication_type_list = request.POST["publication_type_list"] if request.POST[
                                                                                 "publication_type_list"] != "" else None
            location_list = request.POST["location_list"] if request.POST["location_list"] != "" else None
            min_cited_by = request.POST["min_cited_by"] if request.POST["min_cited_by"] != "" else None
            max_cited_by = request.POST["max_cited_by"] if request.POST["max_cited_by"] != "" else None
            language_list = request.POST["language_list"] if request.POST["language_list"] != "" else None

            delimeter = ','
            filter_list = []

            if year_min is not None or year_max is not None:
                if year_min is not None and year_max is not None and year_max <= year_min:
                    is_error = True
                    error_message = "Minimum date cannot be equal to or greater than maximum date"
                else:
                    criterion_param[constants.YEAR][constants.min_year] = year_min
                    criterion_param[constants.YEAR][constants.max_year] = year_max
                    filter_list.append(constants.YEAR)

            if min_impact_factor is not None or max_impact_factor is not None:
                if min_impact_factor is not None and max_impact_factor is not None and min_impact_factor >= max_impact_factor:
                    is_error = True
                    error_message = "Minimum impact factor cannot be equal to or greater than maximum impact factor"
                else:
                    criterion_param[constants.IMPACT_FACTOR][
                        constants.max_impact] = max_impact_factor
                    criterion_param[constants.IMPACT_FACTOR][
                        constants.min_impact] = min_impact_factor
                    filter_list.append(constants.IMPACT_FACTOR)

            if journal_list is not None:
                journal_list = journal_list.strip()
                lists = journal_list.split(delimeter)
                if len(lists) > 0:
                    criterion_param[constants.JOURNAL][constants.journal_list] = lists
                else:
                    is_error = True
                    error_message = "Cannot parse journal list properly, delimit with ,"

            if min_h_index is not None or max_h_index is not None:
                if max_h_index is not None and max_h_index is not None and min_h_index >= max_h_index:
                    is_error = True
                    error_message = "Minimum h-index factor cannot be equal to or greater than maximum h-index"
                else:
                    criterion_param[constants.H_INDEX][
                        constants.max_h_index] = max_h_index
                    criterion_param[constants.H_INDEX][
                        constants.min_h_index] = max_h_index
                    filter_list.append(constants.H_INDEX)

            if publication_type_list is not None:
                publication_type_list = publication_type_list.strip()
                lists = publication_type_list.split(delimeter)
                if len(lists) > 0:
                    criterion_param[constants.PUBLICATION_TYPE][constants.publication_type_list] = lists
                else:
                    is_error = True
                    error_message = "Cannot parse publication types properly, delimit with ,"

            if location_list is not None:
                location_list = location_list.strip()
                lists = location_list.split(delimeter)
                if len(lists) > 0:
                    criterion_param[constants.LOCATION][constants.location_list] = lists
                else:
                    is_error = True
                    error_message = "Cannot parse locations properly, delimit with ,"

            if min_cited_by is not None or max_cited_by is not None:
                if min_cited_by is not None and max_cited_by is not None and min_cited_by >= max_cited_by:
                    is_error = True
                    error_message = "Minimum nn-cited cannot be equal to or greater than maximum n-cited"
                else:
                    criterion_param[constants.N_CITED_BY][
                        constants.max_cited_by] = max_cited_by
                    criterion_param[constants.N_CITED_BY][
                        constants.min_cited_by] = min_cited_by
                    filter_list.append(constants.N_CITED_BY)

            if language_list is not None:
                language_list = language_list.strip()
                lists = language_list.split(delimeter)
                if len(lists) > 0:
                    criterion_param[constants.LANGUAGE][constants.language_list] = lists
                else:
                    is_error = True
                    error_message = "Cannot parse languages properly, delimit with ,"

            if is_error:
                pass
            else:
                shit_object = SLR_Automation(search_query, backward_snowballing_paper_string, filter_list,
                                             criterion_param)
                if title_similarity_score != "":
                    shit_object.title_similarity_score = title_similarity_score
                if abstract_similarity_score != "":
                    shit_object.abstract_similarity_score = abstract_similarity_score
                if forward_snowballing_target != "":
                    shit_object.forward_snowballing_target_papers = forward_snowballing_target
                if forward_snowballing_levels != "":
                    shit_object.forward_snowballing_levels = forward_snowballing_levels
                if backward_snowballing_levels != "":
                    shit_object.backward_snowballing_levels = backward_snowballing_levels

                return render(request, 'slr_automation_ui/results.html', {'results': results})

        # if a GET (or any other method) we'll create a blank form
    else:
        form = SLRForm()
        form.fields["year_min"].widget = DatePickerInput()
        form.fields["year_max"].widget = DatePickerInput()

    return render(request, 'slr_automation_ui/slrform_form.html', {'form': form})
