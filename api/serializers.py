from rest_framework import serializers
from api.models import File


class FileSerializer(serializers.ModelSerializer):
    """Сериализатор модели Файл"""
    class Meta:
        model = File
        fields = '__all__'
