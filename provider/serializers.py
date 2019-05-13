from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    SerializerMethodField
)

from .models import Provider, Service


class ProviderListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="api:provider:provider_services",
        read_only=True,
        lookup_field="uuid"
    )

    class Meta:
        model = Provider
        fields = [
            "url",
            "name",
            "image",
            "height_field",
            "width_field",
            "uuid",
            "created",
            "id",
            "updated"
        ]


class ServiceListSerializer(ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'

