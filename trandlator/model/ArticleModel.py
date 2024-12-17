from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, default='empty title')
    content = models.TextField(default='empty content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 티커
    views = models.PositiveIntegerField(default=0)
    origin_url = models.URLField(max_length=200, blank=True)
