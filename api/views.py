from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Article
from .serializers import *


@api_view(['GET'])
def index(request, name):

    try:
        objs = Article.objects.filter(team0=name) | Article.objects.filter(team1=name)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ArticleSerializer(objs, many=True)
    return Response(serializer.data)
