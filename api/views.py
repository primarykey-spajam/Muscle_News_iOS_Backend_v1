# coding: utf-8
import django_filters
import os

from .models import User, News
from .serializer import UserSerializer, NewsSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import get_voice

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
        obj=User.objects.filter(userId=1)
        # obj=User.objects.filter(id=1)
        serializers = UserSerializer(obj, many=False)
        return Response(serializers.data, status.HTTP_200_OK)

class Voiceet(APIView):
    serializer_class=NewsSerializer

    def create(self, request, format=None):
        mp3_file = get_voice(request['anqResult'])
        path = os.path.join(UPLOAD_DIR, file.name)
        destination = open(path, 'wb')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()

        news, created = News.objects.get_or_create(filepath=path)

        if created:
            news.save()
        return Response({'voice_path': path})
