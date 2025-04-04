from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=100, default='empty title')
    content = models.TextField(default='empty content')
    summary = models.TextField(default='empty summary')
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)
    views = models.PositiveIntegerField(default=0)
    origin_url = models.URLField(max_length=200, blank=True, unique=True)
    tts_content = models.TextField(default='empty tts content')
    tts_url = models.URLField(max_length=200, blank=True)