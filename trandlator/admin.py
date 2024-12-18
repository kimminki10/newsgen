from django.contrib import admin
from trandlator.model.ArticleModel import Article
from trandlator.model.TickerModel import Ticker
from trandlator.model.UserModel import User

admin.site.register(Article)
admin.site.register(Ticker)
admin.site.register(User)