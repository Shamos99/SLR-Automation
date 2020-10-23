from django.views.generic import CreateView
from django.template import loader
from .models import Slrform
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SLRForm
from bootstrap_datepicker_plus import DatePickerInput
from .combine_all import SLR_Automation


def slr_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SLRForm(request.POST)


        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            search_query = request.POST["search_query"]
            backward_snowballing_paper_string = request.POST['backward_snowballing_paper_string']
            title_similarity_score = request.POST['title_similarity_score']
            abstract_similarity_score = request.POST['abstract_similarity_score']
            forward_snowballing_target = request.POST['forward_snowballing_target']
            forward_snowballing_levels =  request.POST['forward_snowballing_levels']
            backward_snowballing_levels = request.POST['backward_snowballing_levels']
            filename_to_store_result = request.POST['filename_to_store_result']
            year_min = request.POST['year_min']
            year_max =  request.POST['year_max']
            min_impact_factor = request.POST['min_impact_factor']
            max_impact_factor = request.POST['max_impact_factor']
            journal_list = request.POST["journal_list"]
            min_h_index = request.POST["min_h_index"]
            max_h_index = request.POST["max_h_index"]
            publication_type_list = request.POST["publication_type_list"]
            location_list = request.POST["location_list"]
            min_cited_by = request.POST["min_cited_by"]
            max_cited_by = request.POST["max_cited_by"]
            language_list = request.POST["language_list"]

            return render(request,'slr_automation_ui/results.html',{'results':results})

        # if a GET (or any other method) we'll create a blank form
    else:
        form = SLRForm()
        form.fields["year_min"].widget = DatePickerInput()
        form.fields["year_max"].widget = DatePickerInput()

    return render(request, 'slr_automation_ui/slrform_form.html', {'form': form})
