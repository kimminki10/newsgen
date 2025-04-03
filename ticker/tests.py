from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from .models import Ticker

# Create your tests here.
class TickerTest(TestCase):
    def test_ticker_creation(self):
        """
        Ticker 모델 생성 테스트
        """
        ticker = Ticker.objects.create(ticker_name="AAPL")
        self.assertEqual(ticker.ticker_name, "AAPL")

    def test_ticker_create_view(self):
        """
        Ticker 생성 뷰 테스트
        """
        client = Client()
        response = client.post(reverse('ticker:create'), {'ticker_name': 'AAPL'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Ticker.objects.filter(ticker_name='AAPL').exists())


