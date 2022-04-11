from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets, permissions
from .models import ApplicationProcessing

from .serializers import UserUploadSerializer, DataUserSerializer
from .services.data_processing import DataProcessing


class UserUploadViewSet(viewsets.ViewSet):
    serializer_class = UserUploadSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request: Request):
        user_url = request.data.get('user_url')
        user_email = request.data.get('user_email')

        return DataProcessing.processing_request(user_url, user_email)

    def list(self, request):
        queryset = ApplicationProcessing.objects.all()
        serializer = DataUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request) -> Response:
        return Response({'serializer': UserUploadSerializer})
