from django.contrib import admin
from .models import Ticker

class TickerAdmin(admin.ModelAdmin):
    list_display = ('ticker_name', 'last_price')
    search_fields = ('ticker_name',)


admin.site.register(Ticker, TickerAdmin)