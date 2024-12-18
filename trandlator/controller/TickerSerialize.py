from rest_framework import serializers
from ..model.TickerModel import Ticker
from .ArticleSerializer import ArticleSerializer

# Ticker 모델 Serializer
class TickerSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = Ticker
        fields =  '__all__'
