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

from .models import Provider
from .serializers import ProviderListSerializer

class ProviderListAPIView(ListAPIView):
	queryset = Provider.objects.all()
	serializer_class = ProviderListSerializer

