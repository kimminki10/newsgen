from django.db import models
from .TickerModel import Ticker

class User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    tickers = models.ManyToManyField(Ticker, related_name='courses',blank=True)
    password=models.CharField(max_length = 256)

    def __str__(self):
        return self.name