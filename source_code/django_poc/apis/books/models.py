from django.db import models


from apis.authors.models import Authors
from apis.category.models import Category
from apis.publisher.models import Publisher

class Books(models.Model):
    book_language_choices = (
        ('Hindi', 'Hindi'),
        ('English', 'English'),
        ('Other', 'Other')
    )
    book_availability_choices = (
        ('Online Reading', 'Online Reading'),
        ('In Library', 'In Library'),
        ('On Rent', 'On Rent'),
        ('For Sell', 'For Sell')
    )

    book_name = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, related_name="book_publisher_id", null=True, blank=True, on_delete=models.CASCADE)
    book_category = models.ForeignKey(Category, related_name="book_category_id", null=True, blank=True, on_delete=models.CASCADE)
    book_language = models.CharField(choices=book_language_choices, max_length=50)
    book_availability = models.CharField(choices=book_availability_choices, max_length=50)
    book_description = models.CharField(max_length=500)

    class Meta:
        db_table = 'tbl_books'

    def __unicode__(self):
        return '%s' % (self.book_name)


class BookAuthorLink(models.Model):
    book = models.ForeignKey(Books, related_name="book_id", on_delete=models.CASCADE)
    author = models.ForeignKey(Authors, related_name="author_id", on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_book_author_link'

    def __unicode__(self):
        return '%s %s' % (self.book.book_name, self.author.first_name)