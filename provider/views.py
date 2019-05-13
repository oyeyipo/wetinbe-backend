from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
    ListAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Provider, Service
from .serializers import ProviderListSerializer, ServiceListSerializer


class ProviderListAPIView(ListAPIView):
    lookup_field = "uuid"
    serializer_class = ProviderListSerializer
    permision_classes = []

    def get_queryset(self):
        return Provider.objects.all()


class ServiceListAPIView(ListAPIView):
    serializer_class = ServiceListSerializer
    permission_classes = []

    def get_queryset(self):
        return Service.objects.all()

class ProviderServicesListAPIView(ListAPIView):
    lookup_field = 'uuid'
    permission_classes = []

    def get_serializer_class(self):
        return ServiceListSerializer

    def get_queryset(self):
        uuid = self.kwargs[self.lookup_field]
        provider = get_object_or_404(Provider, uuid=uuid)
        obj = provider.services.all()
        return obj




