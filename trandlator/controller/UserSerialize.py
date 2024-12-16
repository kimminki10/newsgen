# Define a serializer for UserItem

from rest_framework import serializers
from ..model.UserModel import UserItem


class UserItemSerializer(serializers.Serializer):
    class Meta:
        model = UserItem
        fields = '__all__'  # Include all fields of the model. Adjust as needed.