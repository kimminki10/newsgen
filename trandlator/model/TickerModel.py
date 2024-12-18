from django.db import models
from .ArticleModel import Article
# 티커

class Ticker(models.Model):
    ticker_name = models.CharField(max_length=100, unique=True)
    articles = models.ManyToManyField(Article, related_name='tickers',blank=True)

    def __str__(self):
        return self.ticker_name
    


