from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

from geoanswers import api
from munigeo.api import AdministrativeDivisionViewSet

router = DefaultRouter()
router.register(r'respondents', api.RespondentViewSet)
router.register(r'answers', api.MapAnswerViewSet)
router.register(r'divisions', AdministrativeDivisionViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls))
)
