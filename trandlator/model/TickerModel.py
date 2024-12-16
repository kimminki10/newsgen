from django.db import models

# 티커

class Ticker(models.Model):
    ticker_name = models.CharField(max_length=100, unique=True)
    article_list = models.ManyToManyField('Article', related_name='tickers', blank=True)  # Article과 연결
    ticker_id = models.AutoField(primary_key=True)  # 자동 증가 ID

    def __str__(self):
        return self.ticker_name
    


