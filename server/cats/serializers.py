from rest_framework import serializers
from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Cat
        exclude = ['owner', '_photo']

    def create(self, validated_data):
        user = self.context['request'].user
        return Cat.objects.create(owner=user, **validated_data)
