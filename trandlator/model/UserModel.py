from django.db import models

# 티커
class Ticker(models.Model):
    ticker_name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.ticker_name

class User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    tickers = models.ManyToManyField(Ticker,related_name='interested_users', blank =True)
    password=models.CharField(max_length = 256)


    def __str__(self):
        return self.name