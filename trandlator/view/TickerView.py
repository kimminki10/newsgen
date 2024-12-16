from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..model.TickerModel import Ticker
from ..controller.TickerSerializer import TickerSerializer

class TickerListView(APIView):
    """
    GET: 전체 티커 목록 조회 
    POST: 새로운 티커 데이터 생성
    """
    def get(self, request):
        """
        Query Params로 필터링된 티커 목록 반환
        """
        title = request.GET.get('title')  
        
        if title:
            tickers = Ticker.objects.filter(ticker_name__icontains=title)
        else:
            tickers = Ticker.objects.all()
        
        serializer = TickerSerializer(tickers, many=True)
        return Response({"success": True, "tickers": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        새로운 Ticker 객체 생성
        """
        serializer = TickerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "ticker": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
