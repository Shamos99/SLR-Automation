from django.db import models

# Create your models here.
class Slrform(models.Model):
    search_query = models.CharField(max_length=1000)
    backward_snowballing_paper_string = models.CharField(max_length=1000)
    title_similarity_score = models.IntegerField(blank=True)
    abstract_similarity_score = models.IntegerField(blank=True)
    forward_snowballing_target = models.IntegerField(blank=True)
    forward_snowballing_levels = models.IntegerField(blank=True)
    backward_snowballing_levels = models.IntegerField(blank=True)
    backward_snowballing_target = models.IntegerField(blank=True)
    filename_to_store_result = models.CharField(max_length=1000,blank=True)
    year_min = models.DateField(blank=True)
    year_max = models.DateField(blank=True)
    min_impact_factor = models.IntegerField(blank=True)
    max_impact_factor = models.IntegerField(blank=True)
    journal_list = models.TextField(blank=True)
    min_h_index = models.IntegerField(blank=True)
    max_h_index = models.IntegerField(blank=True)
    publication_type_list =  models.TextField(blank=True)
    location_list = models.TextField(blank=True)
    min_cited_by= models.IntegerField(blank=True)
    max_cited_by = models.IntegerField(blank=True)
    language_list = models.TextField(blank=True)


