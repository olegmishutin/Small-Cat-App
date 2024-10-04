from rest_framework import serializers
from django.contrib.auth import get_user_model
from .validators import validate_password
from django.contrib.auth.models import AbstractUser


class RegistrationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {
                'validators': [validate_password]
            }
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
