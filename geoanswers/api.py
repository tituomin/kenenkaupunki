
from rest_framework import viewsets

from .serializers import RespondentSerializer, MapAnswerSerializer
from .models import Respondent, MapAnswer

class RespondentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Respondents to the questionnaire.

    """
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
    filter_fields = ['neighborhood']

class MapAnswerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    MapAnswers to the questionnaire.

    """
    queryset = MapAnswer.objects.all()
    serializer_class = MapAnswerSerializer
    filter_fields = ['respondent__neighborhood']
