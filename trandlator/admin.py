from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from .models import Article, Ticker, User
from django.urls import path
from crawling.services.set_tickers import add_new_tickers
from crawling.services.set_articles import add_new_articles

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'origin_url', 'created_at')
    search_fields = ('title', 'content')
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('crawl-article/', self.admin_site.admin_view(self.crawl_article), name='crawl-article'),
        ]
        return custom_urls + urls

    def crawl_article(self, request):
        self.message_user(request, "Article crawling started.")
        print("Article crawling started.")
        count = add_new_articles()
        self.message_user(request, f"Article data has been crawled. {count} articles have been added.")
        print(f"Article data has been crawled. {count} articles have been added.")
        return HttpResponseRedirect("../")

    def crawl_article_button(self, obj):
        return format_html('<a class="button" href="{}">Crawl Article</a>', reverse('admin:crawl-article'))

    crawl_article_button.short_description = 'Crawl Article'
    crawl_article_button.allow_tags = True

    change_list_template = "admin/article_changelist.html"


class TickerAdmin(admin.ModelAdmin):
    list_display = ('ticker_name', 'last_price')
    search_fields = ('ticker_name',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('crawl-ticker/', self.admin_site.admin_view(self.crawl_ticker), name='crawl-ticker'),
        ]
        return custom_urls + urls

    def crawl_ticker(self, request):
        self.message_user(request, "Ticker crawling started.")
        crawled_ticker_count = add_new_tickers()
        self.message_user(request, f"Ticker data has been crawled. count: {crawled_ticker_count}")
        return HttpResponseRedirect("../")

    def crawl_ticker_button(self, obj):
        return format_html('<a class="button" href="crawl_ticker">Crawl Ticker</a>', reverse('admin:crawl_ticker'))
    
    crawl_ticker_button.short_description = "Crawl Ticker Data"
    crawl_ticker_button.allow_tags = True

    change_list_template = "admin/ticker_change_list.html"


admin.site.register(Article, ArticleAdmin)
admin.site.register(Ticker, TickerAdmin)
admin.site.register(User)