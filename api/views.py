# coding: utf-8
import django_filters
import os

from .models import News
from .serializer import NewsSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

UPLOAD_DIR = 'media/newsVoices/'
# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
