from django.urls import path


from . import views

urlpatterns = [
    path('', views.slr_form, name='PersonCreateView'),
]