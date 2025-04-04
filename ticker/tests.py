from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ticker.models import Ticker
from article.models import Article
from datetime import datetime, timedelta
import json
from django.utils import timezone


class TickerViewsTestCase(TestCase):
    def setUp(self):
        """테스트 시작 전 실행되는 설정 메소드"""
        # 테스트용 API 클라이언트 생성
        self.client = APIClient()
        
        # 테스트에 필요한 모의 Article 객체 생성
        self.article1 = Article.objects.create(
            title='Sample Article 1',
            content='Content 1',
            summary='Summary 1',
            origin_url='https://example.com/1'
        )
        
        self.article2 = Article.objects.create(
            title='Sample Article 2',
            content='Content 2',
            summary='Summary 2',
            origin_url='https://example.com/2'
        )

        now = timezone.now()
        yesterday = now - timedelta(days=1)
        
        # 테스트용 Ticker 객체들 생성
        self.ticker1 = Ticker.objects.create(
            ticker_name='AAPL',
            last_price=150.25,
            before_last_price=148.50,
            price_diff=1.75,
            percentage_diff=1.18,
            last_price_date=now,
            before_last_date=yesterday,
        )
        self.ticker1.articles.add(self.article1)
        
        self.ticker2 = Ticker.objects.create(
            ticker_name='MSFT',
            last_price=280.75,
            before_last_price=275.20,
            price_diff=5.55,
            percentage_diff=2.02,
            last_price_date=now,
            before_last_date=yesterday,
        )
        self.ticker2.articles.add(self.article1, self.article2)
        
        self.ticker3 = Ticker.objects.create(
            ticker_name='GOOGL',
            last_price=2750.30,
            before_last_price=2720.15,
            price_diff=30.15,
            percentage_diff=1.11,
            last_price_date=now,
            before_last_date=yesterday,
        )
        
        # URL 경로 (ticker/urls.py 확인 결과)
        self.list_url = reverse('ticker-list')  # /ticker/
        
    def test_get_all_tickers(self):
        """모든 Ticker 객체 조회 테스트"""
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
    
    def test_create_ticker(self):
        """새 Ticker 객체 생성 테스트"""
        data = {
            'ticker_name': 'AMZN',
            'last_price': 3300.50,
            'before_last_price': 3275.25,
            'price_diff': 25.25,
            'percentage_diff': 0.77,
        }
        
        response = self.client.post(
            self.list_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['ticker_name'], 'AMZN')
        self.assertEqual(Ticker.objects.count(), 4)
    
    def test_get_single_ticker(self):
        """특정 Ticker 객체 조회 테스트"""
        detail_url = reverse('ticker-detail', kwargs={'ticker_name': 'AAPL'})
        response = self.client.get(detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ticker_name'], 'AAPL')
        self.assertEqual(response.data['last_price'], 150.25)
        # 연결된 기사 수 확인
        self.assertEqual(len(response.data['articles']), 1)
    
    def test_update_ticker(self):
        """Ticker 객체 업데이트 테스트"""
        detail_url = reverse('ticker-detail', kwargs={'ticker_name': 'MSFT'})
        data = {
            'ticker_name': 'MSFT',
            'last_price': 285.50,
            'before_last_price': 280.75,
            'price_diff': 4.75,
            'percentage_diff': 1.69
        }
        
        response = self.client.put(
            detail_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['last_price'], 285.50)
        self.assertEqual(response.data['price_diff'], 4.75)
    
    def test_partial_update_ticker(self):
        """Ticker 객체 부분 업데이트 테스트"""
        detail_url = reverse('ticker-detail', kwargs={'ticker_name': 'GOOGL'})
        data = {
            'last_price': 2800.00,
            'price_diff': 79.85
        }
        
        response = self.client.patch(
            detail_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['last_price'], 2800.00)
        self.assertEqual(response.data['price_diff'], 79.85)
        # 변경하지 않은 필드 확인
        self.assertEqual(response.data['before_last_price'], 2720.15)
    
    def test_delete_ticker(self):
        """Ticker 객체 삭제 테스트"""
        detail_url = reverse('ticker-detail', kwargs={'ticker_name': 'GOOGL'})
        initial_count = Ticker.objects.count()
        
        response = self.client.delete(detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ticker.objects.count(), initial_count - 1)
        with self.assertRaises(Ticker.DoesNotExist):
            Ticker.objects.get(ticker_name='GOOGL')
    
    def test_get_nonexistent_ticker(self):
        """존재하지 않는 Ticker 객체 조회 테스트"""
        detail_url = reverse('ticker-detail', kwargs={'ticker_name': 'NONEXISTENT'})
        response = self.client.get(detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_article_relationship(self):
        """Ticker와 Article 간의 관계 테스트"""
        # MSFT 티커는 두 개의 기사와 연결되어 있어야 함
        msft = Ticker.objects.get(ticker_name='MSFT')
        self.assertEqual(msft.articles.count(), 2)
        
        # AAPL 티커는 한 개의 기사와 연결되어 있어야 함
        aapl = Ticker.objects.get(ticker_name='AAPL')
        self.assertEqual(aapl.articles.count(), 1)
        
        # GOOGL 티커는 기사가 없어야 함
        googl = Ticker.objects.get(ticker_name='GOOGL')
        self.assertEqual(googl.articles.count(), 0)