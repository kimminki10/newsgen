from rest_framework import serializers
from ..model.TickerModel import Ticker

# Ticker 모델 Serializer
class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ['ticker_id', 'ticker_name', 'article_list']
        extra_kwargs = {
            'ticker_id': {'read_only': True},  # 자동 증가 필드이므로 읽기 전용
            'ticker_name': {'required': True},  # 필수 입력 필드
        }

    def create(self, validated_data):
        """
        Ticker 객체 생성
        """
        article_list = validated_data.pop('article_list', [])  # ManyToMany 관계 처리
        ticker = Ticker.objects.create(**validated_data)  # Ticker 객체 생성
        ticker.article_list.set(article_list)  # 관계 설정
        return ticker

    def update(self, instance, validated_data):
        """
        Ticker 객체 업데이트
        """
        instance.ticker_name = validated_data.get('ticker_name', instance.ticker_name)

        if 'article_list' in validated_data:
            article_list = validated_data.pop('article_list')
            instance.article_list.set(article_list)  # ManyToMany 관계 업데이트

        instance.save()
        return instance