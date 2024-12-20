from django.contrib import admin
from .models import Article
from .models import Ticker
from .models import User

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'origin_url', 'created_at')
    search_fields = ('title', 'content')


class TickerAdmin(admin.ModelAdmin):
    list_display = ('ticker_name', 'last_price')
    search_fields = ('ticker_name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Ticker, TickerAdmin)
admin.site.register(User)