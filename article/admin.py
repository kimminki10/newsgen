from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'origin_url', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Article, ArticleAdmin)