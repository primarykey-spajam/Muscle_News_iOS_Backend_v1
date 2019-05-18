from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    anqResult = models.CharField(max_length=30)

class News(models.Model):
    newsId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    newsText = models.TextField()
    newsVoice = models.FileField()
    textType = models.CharField(max_length=30)
