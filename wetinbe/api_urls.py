from django.urls import path, include


app_name='wetinbe'
urlpatterns = [
	# API URLs
	path("providers/", include("provider.urls", namespace="provider")),
]