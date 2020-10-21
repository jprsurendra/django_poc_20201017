from rest_framework import serializers
from .models import Authors

class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        name = obj.first_name
        if obj.last_name:
            name = name + ' ' + obj.last_name
        return name

    class Meta:
        model = Authors
        fields = '__all__'