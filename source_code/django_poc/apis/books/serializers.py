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

    # Create the Books instance
    def create(self, validated_data):
        book_id = validated_data.get('id', None)
        if book_id:
            instance = Books.objects.get(id=book_id)
            instance.book_name = validated_data['book_name']
            instance.publisher_id = validated_data['publisher_id']
            instance.book_category_id = validated_data['book_category_id']
            instance.book_language = validated_data['book_language']
            instance.book_availability = validated_data.get('book_language_other_value','')
            instance.book_description = validated_data['book_description']
            instance.save()
        else:
            instance = Books.objects.create( book_name = validated_data['book_name'],
                                             publisher_id = validated_data['publisher_id'],
                                             book_category_id = validated_data['book_category_id'],
                                             book_language = validated_data['book_language'],
                                             book_availability = validated_data.get('book_language_other_value', ''),
                                             book_description = validated_data['book_description']
                                        )
        return instance

    # Update the Books instance
    # def update(self, instance, validated_data):
    #     instance.title = validated_data['title']
    #     instance.save()
    #     return instance