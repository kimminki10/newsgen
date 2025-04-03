from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    tickers = serializers.SerializerMethodField()
    def get_tickers(self, obj):
        return [ticker.ticker_name for ticker in obj.tickers.all()]

    class Meta:
        model = Article
        fields = '__all__'