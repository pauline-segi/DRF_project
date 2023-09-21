from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields ='__all__'
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        token, created = Token.objects.get_or_create(user=user)
        return user


