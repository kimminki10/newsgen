from django.urls import path
from .views import TickerListCreateView, TickerDetailView

urlpatterns = [
    path('', TickerListCreateView.as_view(), name='ticker-list'),
    path('<str:ticker_name>/', TickerDetailView.as_view(), name='ticker-detail'),
]
