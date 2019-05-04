"""Defines URLS patters for Build_logs"""

from django.conf.urls import url

from . import views

app_name = 'build_log'

urlpatterns = [
    # Homepage
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?<topic_id>\d+)/$', views.topic, name="topic"),
]