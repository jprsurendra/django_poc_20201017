from rest_framework import serializers
from .models import Publisher

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class PublisherNameSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    publisher_name = serializers.CharField()