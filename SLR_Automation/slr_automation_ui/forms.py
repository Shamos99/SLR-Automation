from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from slr_automation_ui.models import Slrform
from django.contrib.admin import widgets

class SLRForm(forms.ModelForm):
    # search_query = forms.CharField(max_length=200)
    # backward_snowballing_paper_string = forms.CharField(max_length=200)
    # title_similarity_score = forms.IntegerField()
    # abstract_similarity_score = forms.IntegerField()
    # forward_snowballing_target = forms.IntegerField()
    # forward_snowballing_levels = forms.IntegerField()
    # backward_snowballing_levels = forms.IntegerField()
    # filename_to_store_result = forms.FileField()
    # year_min = forms.DateField()
    # year_max = forms.DateField()
    # min_impact_factor = forms.IntegerField()
    # max_impact_factor = forms.IntegerField()
    # journal_list = forms.Textarea()
    # min_h_index = forms.IntegerField()
    # max_h_index = forms.IntegerField()
    # publication_type_list = forms.Textarea()
    # location_list = forms.Textarea()
    # min_cited_by = forms.IntegerField()
    # max_cited_by = forms.IntegerField()
    # language_list = forms.Textarea()
    #

    class Meta:
        model = Slrform
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SLRForm, self).__init__(*args, **kwargs)
        self.fields['year_min'].widget = widgets.AdminDateWidget()
        self.fields['year_max'].widget = widgets.AdminDateWidget()

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))
