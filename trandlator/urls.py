from django.contrib import admin
from django.urls import path
from trandlator.view.UserView import UserView,UserTickers
from trandlator.view.TickerView import TickerView


urlpatterns = [
    #path('', test, name='home'),  # 루트 경로 ("/")
    path('admin/', admin.site.urls),  # Django 관리자 페이지
    path('user/', UserView.as_view(), name='user'),
    path('user/tickers/', UserTickers.as_view(), name='user_tickers'),
    path('ticker/', TickerView.as_view(), name='ticker'),
]
