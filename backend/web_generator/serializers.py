from rest_framework.serializers import (Serializer, URLField, EmailField, ModelSerializer)
from rest_framework import serializers
from .models import ApplicationProcessing


class UserUploadSerializer(Serializer):
    user_url = URLField()
    user_email = EmailField()

    class Meta:
        fields = ['user_url', 'user_email']


class DataUserSerializer(ModelSerializer):
    user_url = serializers.CharField(source='user_url.url')
    user = serializers.CharField(source='user.email')

    class Meta:
        model = ApplicationProcessing
        status_dict = {
            1: 'Data loading',
            2: 'In progress',
            3: 'Finish'
        }
        fields = ['id', 'create_datetime', 'status', 'user', 'user_url']
