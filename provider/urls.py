from django.urls import path

from .views import (
	ProviderListAPIView
)


app_name='Provider'
urlpatterns = [
	path("", ProviderListAPIView.as_view(), name="list"),
]