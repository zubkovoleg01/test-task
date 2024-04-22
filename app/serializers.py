from rest_framework import serializers
from .models import Cinemas

class CinemasSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Cinemas
    """
    class Meta:
        model = Cinemas
        fields = '__all__'
