from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from mozio_library.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields=['id', 'name', 'email', 'phone_number', 'language', 'currency']

class ServiceAreaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ServiceArea
        geo_field = "poly"
        fields = ['id', 'provider', 'name', 'price', 'poly']
        
class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ['id', 'provider','name', 'price']