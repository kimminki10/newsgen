from django.db import models

class Article(models.Model):
    name = "aa"

    def __str__(self):
        return self.name
# 티커

class Ticker(models.Model):
    ticker_name = models.CharField(max_length=100, unique=True)
    articles = models.ManyToManyField(Article, related_name='courses',blank=True)  # Article과 연결

    def __str__(self):
        return self.name
    


