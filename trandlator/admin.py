from django.contrib import admin
from .models import Article
from .models import Ticker
from .models import User

admin.site.register(Article)
admin.site.register(Ticker)
admin.site.register(User)