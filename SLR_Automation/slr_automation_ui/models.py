from django.db import models

# Create your models here.
class Slrform(models.Model):
    search_query = models.CharField(max_length=200)
    backward_snowballing_paper_string = models.CharField(max_length=200)
    title_similarity_score = models.IntegerField()
    abstract_similarity_score = models.IntegerField()
    forward_snowballing_target = models.IntegerField()
    forward_snowballing_levels = models.IntegerField()
    backward_snowballing_levels = models.IntegerField()
    filename_to_store_result = models.CharField(max_length=200)
    year_min = models.DateField()
    year_max = models.DateField()
    min_impact_factor = models.IntegerField()
    max_impact_factor = models.IntegerField()
    journal_list = models.TextField()
    min_h_index = models.IntegerField()
    max_h_index = models.IntegerField()
    publication_type_list =  models.TextField()
    location_list = models.TextField()
    min_cited_by= models.IntegerField()
    max_cited_by = models.IntegerField()
    language_list = models.TextField()


