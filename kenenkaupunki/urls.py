from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

from geoanswers import api
from munigeo.api import AdministrativeDivisionViewSet

urlpatterns = patterns(
    'geoanswers.api',
    url(r'^divisions/$', 'division_list'),
    url(r'^divisions/(?P<pk>[0-9]+)$', 'individual_division'),
    url(r'^respondents/$', 'respondent_list'),
    url(r'^respondents/(?P<pk>[0-9]+)$', 'individual_respondent'),
    url(r'^answers/$', 'mapanswer_list')
)
