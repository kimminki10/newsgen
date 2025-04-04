from django.db import models
from django.utils import timezone
from article.models import Article


class Ticker(models.Model):
    ticker_name = models.CharField(max_length=100, unique=True)
    articles = models.ManyToManyField(Article, related_name='tickers',blank=True)
    last_price = models.FloatField(default=0)
    before_last_price = models.FloatField(default=0)
    price_diff = models.FloatField(default=0)
    percentage_diff = models.FloatField(default=0)
    last_price_date = models.DateTimeField(default=timezone.now, blank=True)
    before_last_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.ticker_name
