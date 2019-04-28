from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	HyperlinkedRelatedField,
	SerializerMethodField
)

from .models import Provider

class ProviderListSerializer(ModelSerializer):
	class Meta:
		model = Provider
		fields ='__all__'