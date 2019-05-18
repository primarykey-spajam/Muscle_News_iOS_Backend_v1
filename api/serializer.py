from rest_framework import serializers
from .models import User, News


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ("userId", "favorite")

class NewsSerializer(serializers.Serializer):
    class Meta:
        model = News
        fields = ("newsId", "newsText", "newsFile", "textType")
