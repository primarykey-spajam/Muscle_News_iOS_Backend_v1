# coding: utf-8
import django_filters
import os

from .models import User, News
from .serializer import UserSerializer, NewsSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from get_voice import

UPLOAD_DIR = 'media/newsVoices/'
# Create your views here.

# class NewsViewSet(APIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

class UserGet(APIView):
    # http://flame-blaze.net/archives/4999
    # request must have PARAMS['id']
    def get(self, request, format=None):
        obj=User.objects.filter(userId=request.PARAMS["userId"])
        # obj=User.objects.filter(id=1)
        serializers = UserSerializer(obj, many=False)
        return Response(serializers.data, status.HTTP_200_OK)
