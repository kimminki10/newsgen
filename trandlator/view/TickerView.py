from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from ..models import Ticker
from ..controller.TickerSerialize import TickerSerializer


class TickerView(APIView):
    """
    GET: 전체 티커 목록 조회 
    POST: 새로운 티커 데이터 생성
    """

    def get(self, request):
        """
        {
            "ticker_name": "ticker"
        }
        Query Params로 필터링된 Ticker 객체 반환

        아무런 파라미터 없이 요청시 전체 Ticker 목록 반환
        """
        ticker_name = request.data.get('ticker_name')  # Query Params에서 'ticker_name' 가져오기
        
        try:
            if ticker_name:
                # 특정 ticker_name으로 필터링
                ticker = Ticker.objects.get(ticker_name=ticker_name)
                serializer = TickerSerializer(ticker)
                return Response({
                    "success": True,
                    "ticker": serializer.data
                }, status=status.HTTP_200_OK)
            else:
                # ticker_name이 없으면 전체 목록 반환
                tickers = Ticker.objects.all()
                serializer = TickerSerializer(tickers, many=True)
                return Response({
                    "success": True,
                    "tickers": serializer.data
                }, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({
                "success": False,
                "error": f"Ticker with name '{ticker_name}' does not exist."
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        """
        {
            "ticker_name" : "ticker"
        }
        새로운 Ticker 객체 생성
        ticker_name 중복 불가
        """
        print("Ticker Post")
        ticker_name = request.data.get('ticker_name')
        
        try:
            # 유효성 검사
            if not ticker_name:
                return Response({'success': False, 'error': "ticker_name is required"}, 
                                status=status.HTTP_400_BAD_REQUEST)
            
            # Ticker 객체 생성
            ticker = Ticker.objects.create(ticker_name=ticker_name)
            print("Ticker Created:", ticker.ticker_name)

            return Response({'success': True, 'ticker_id': ticker.id}, 
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Error:", str(e))
            return Response({'success': False, 'error': str(e)}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TickerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: 특정 Ticker 객체 조회
    PUT: 특정 Ticker 객체 수정
    DELETE: 특정 Ticker 객체 삭제
    """
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    lookup_field = 'ticker_name'
    lookup_url_kwarg = 'ticker_name'