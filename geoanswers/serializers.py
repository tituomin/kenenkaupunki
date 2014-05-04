
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Respondent, MapAnswer

class RespondentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respondent

class MapAnswerSerializer(GeoFeatureModelSerializer):
    class Meta:
        geo_field = 'geometry'
        model = MapAnswer
        exclude = ["geometry_original"]
