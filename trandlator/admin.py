from django.contrib import admin
from .models import Article
from .models import Ticker
from .models import User

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'origin_url', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Ticker)
admin.site.register(User)