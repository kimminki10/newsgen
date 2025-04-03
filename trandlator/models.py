from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=100, default='empty title')
    content = models.TextField(default='empty content')
    summary = models.TextField(default='empty summary')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    views = models.PositiveIntegerField(default=0)
    origin_url = models.URLField(max_length=200, blank=True, unique=True)
    tts_content = models.TextField(default='empty tts content')
    tts_url = models.URLField(max_length=200, blank=True)


class Ticker(models.Model):
    ticker_name = models.CharField(max_length=100, unique=True)
    articles = models.ManyToManyField(Article, related_name='tickers',blank=True)
    last_price = models.FloatField(default=0)
    before_last_price = models.FloatField(default=0)
    price_diff = models.FloatField(default=0)
    percentage_diff = models.FloatField(default=0)
    last_price_date = models.DateTimeField(default=datetime.now, blank=True)
    before_last_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.ticker_name
