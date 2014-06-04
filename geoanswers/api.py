import django_filters
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from munigeo.models import AdministrativeDivision
from munigeo.api import AdministrativeDivisionSerializer

from .serializers import RespondentSerializer, MapAnswerSerializer
from .models import Respondent, MapAnswer

@api_view(['GET'])
def division_list(request):
    if (request.method != 'GET' or
        'type' not in request.GET):
        return Response(status=status.HTTP_404_NOT_FOUND)

    type_ = request.GET['type']
    divisions = AdministrativeDivision.objects.filter(type=type_)
    serializer = AdministrativeDivisionSerializer(divisions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def individual_division(request, pk):
    if request.method != 'GET':
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        division = AdministrativeDivision.objects.get(pk=pk)
    except AdministrativeDivision.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AdministrativeDivisionSerializer(division)
    return Response(serializer.data)

@api_view(['GET'])
def respondent_list(request):
    if (request.method != 'GET' or
        'neighborhood' not in request.GET):
        return Response(status=status.HTTP_404_NOT_FOUND)

    neighborhood = request.GET['neighborhood']
    respondents = Respondent.objects.filter(neighborhood=neighborhood)
    serializer = RespondentSerializer(respondents, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def individual_respondent(request, pk):
    if request.method != 'GET':
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        respondent = Respondent.objects.get(pk=pk)
    except Respondent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RespondentSerializer(respondent)
    return Response(serializer.data)

@api_view(['GET'])
def mapanswer_list(request):
    if (request.method != 'GET' or
        'category' not in request.GET or
        'respondent__neighborhood' not in request.GET):
        return Response(status=status.HTTP_404_NOT_FOUND)

    neighborhood = request.GET['respondent__neighborhood']
    category = request.GET['category']
    mapanswers = MapAnswer.objects.filter(category=category).filter(
        respondent__neighborhood=neighborhood)
    serializer = MapAnswerSerializer(mapanswers, many=True)
    return Response(serializer.data)
