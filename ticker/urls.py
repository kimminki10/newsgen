from django.urls import path
from .views import TickerView, TickerDetailView

urlpatterns = [
    path('', TickerView.as_view(), name='ticker'),
    path('<str:ticker_name>/', TickerDetailView.as_view(), name='ticker_detail'),
]
