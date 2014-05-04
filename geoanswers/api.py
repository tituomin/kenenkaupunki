import django_filters
from rest_framework import viewsets
from rest_framework import pagination

from .serializers import RespondentSerializer, MapAnswerSerializer
from .models import Respondent, MapAnswer

class RespondentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Respondents to the questionnaire.

    """
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
    # pagination_serializer_class = pagination.BasePaginationSerializer
    # paginate_by = 500
    filter_fields = ['neighborhood']

class MapAnswerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    MapAnswers to the questionnaire.

    """
    queryset = MapAnswer.objects.all()
    serializer_class = MapAnswerSerializer
    filter_fields = ['respondent__neighborhood', 'category']
