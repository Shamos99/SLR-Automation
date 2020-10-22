from django.views.generic import CreateView
from django.template import loader
from .models import Slrform
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SLRForm
from bootstrap_datepicker_plus import DatePickerInput

def slr_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SLRForm(request.POST)


        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = SLRForm()
        form.fields["year_min"].widget = DatePickerInput()
        form.fields["year_max"].widget = DatePickerInput()

    return render(request, 'slr_automation_ui/slrform_form.html', {'form': form})
