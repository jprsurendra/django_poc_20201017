from rest_framework import serializers

from apis.authors.serializers import AuthorSerializer
from apis.books.models import Books
from apis.category.models import Category
from apis.category.serializers import CategorySerializer
from apis.publisher.serializers import PublisherSerializer


class BookSerializer(serializers.ModelSerializer):
    # category_info = serializers.SerializerMethodField(read_only=True)
    book_category = CategorySerializer(read_only=True)
    book_category_id = serializers.IntegerField(write_only=True)

    publisher = PublisherSerializer(read_only=True)
    publisher_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Books
        fields = '__all__'

    # def get_category_info(self, obj):
    #     category= Category.objects.get(id=obj.book_category_id)
    #     return CategorySerializer(category).data