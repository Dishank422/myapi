from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Article
from .serializers import *


@api_view(['GET'])
def sport(request, sport_name):

    try:
        objs = Article.objects.filter(sport=sport_name)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ArticleSerializer(objs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sex(request, s):

    try:
        objs = Article.objects.filter(sex=s)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ArticleSerializer(objs, many=True)
    return Response(serializer.data)
