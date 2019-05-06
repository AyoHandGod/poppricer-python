"""Defines URL patterns for pricer"""

from django.conf.urls import url

from . import views


app_name = 'pricer'

urlpatterns = [
    url(r'^search/$', views.search, name="search"),
    url(r'^search_found/$', views.search_result)
]