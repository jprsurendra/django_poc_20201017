from rest_framework import serializers
from .models import Authors

class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    def get_name(self, obj):
        full_name = obj.first_name
        if obj.last_name:
            full_name = full_name + ' ' + obj.last_name
        return full_name

    class Meta:
        model = Authors
        fields = '__all__'

    # def create(self, validated_data):
    #     book_instance = None
    #     logged_in_user = self.context['request'].user
    #     newly_paid_amount = validated_data.pop('newly_paid_amount', None)
    #     payment_transaction_id = validated_data.pop('payment_transaction_id', None)
    #
    #     return book_instance


class AuthorNameSerializer(serializers.ModelSerializer):
    # name = AuthorSerializer(fields=['id', 'name'])
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        name = obj.first_name
        if obj.last_name:
            name = name + ' ' + obj.last_name
        return name

    class Meta:
        model = Authors
        fields = ['id', 'name']