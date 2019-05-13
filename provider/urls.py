from django.urls import path

from .views import (
    ProviderListAPIView,
    ServiceListAPIView,
    ProviderServicesListAPIView
)


app_name = 'Provider'
urlpatterns = [
	# list all providers
    path("", ProviderListAPIView.as_view(), name="list"),
    # list services of specified Provider
    path("<slug:uuid>/", ProviderServicesListAPIView.as_view(), name="provider_services"),
    # list all services in all
    path("services/", ServiceListAPIView.as_view(), name="service_list"), 
]
