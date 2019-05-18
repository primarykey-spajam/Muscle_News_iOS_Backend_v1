from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.Serializer):
    class Meta:
        model = News
        fields = ("newsId", "newsText", "newsFile", "textType")
