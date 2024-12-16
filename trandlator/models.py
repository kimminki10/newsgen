from django.db import models

# 티커
class Ticker(models.Model):
    ticker_name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.ticker_name
    
# 유저
class User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    interested_tickers = models.ManyToManyField(Ticker,related_name='interested_users', blank =True)
    password=models.CharField(max_length = 256)

    def __str__(self):
        return self.name

# 기사
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    ticker = models.ForeignKey(Ticker,on_delete = models.CASCADE, related_name = 'articles')
    views = models.PositiveBigIntegerField(default = 0)
    source_url = models.URLField(blank= True, null=True)
    summary = models.URLField(blank = True,null=True)
    
    def __str__(self):
        return self.title