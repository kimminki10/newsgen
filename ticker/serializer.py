from rest_framework import serializers
from ticker.models import Ticker
from article.serializer import ArticleSerializer


class TickerSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = Ticker
        fields =  '__all__'

class TickerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields =  ['ticker_name']
        
class TickerNoArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields =  '__all__'