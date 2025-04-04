from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Ticker
from .serializer import TickerSerializer


class TickerListCreateView(ListCreateAPIView):
    serializer_class = TickerSerializer
    queryset = Ticker.objects.all()


class TickerDetailView(RetrieveUpdateDestroyAPIView):
    """
    GET: 특정 Ticker 객체 조회
    PUT: 특정 Ticker 객체 수정
    DELETE: 특정 Ticker 객체 삭제
    """
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    lookup_field = 'ticker_name'
    lookup_url_kwarg = 'ticker_name'