from rest_framework import serializers
from ..model.TickerModel import Ticker

# Ticker 모델 Serializer
class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields =  [ 'ticker_name', 'articles']
        extra_kwargs = {
            'ticker_name': {'required': True}  # 필수 입력 필드
        }

    # 비밀번호를 해시로 저장하도록 커스텀 create 메서드 작성
    def create(self, validated_data):
        ticker = Ticker(
            ticker_name=validated_data['ticker_name'],
            articles=validated_data['articles']
        )
        ticker.save()
        return ticker
