from trandlator.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_email_verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'is_email_verified']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user