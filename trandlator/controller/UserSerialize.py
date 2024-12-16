# Define a serializer for UserItem

from rest_framework import serializers
from ..model.UserModel import User

# json 객체
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password','tickers']
        extra_kwargs = {
            'password': {'write_only': True}  # 비밀번호는 쓰기 전용으로 설정
        }

    # 비밀번호를 해시로 저장하도록 커스텀 create 메서드 작성
    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            email=validated_data['email'],
            tickers=validated_data['tickers']
        )
        user.set_password(validated_data['password'])  # 비밀번호 암호화
        user.save()
        return user