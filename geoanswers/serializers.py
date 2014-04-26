
from rest_framework import serializers
from munigeo.api import GeoModelSerializer
from .models import Respondent, MapAnswer

class RespondentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respondent

class MapAnswerSerializer(GeoModelSerializer):
    class Meta:
        model = MapAnswer
        exclude = ["geometry_original", "type"]

