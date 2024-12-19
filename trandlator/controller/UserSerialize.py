from trandlator.models import User
from rest_framework import serializers
from .TickerSerialize import TickerSerializer

class UserSerializer(serializers.ModelSerializer):
    tickers = TickerSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)
    is_email_verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ['id',
                  'mail_frequency',
                  'mail_timeSlot',
                  'mail_newsCount',
                  'tickers', 
                  'password', 
                  'email', 
                  'is_email_verified']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user