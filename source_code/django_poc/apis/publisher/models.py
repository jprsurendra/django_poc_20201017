from django.db import models

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    class Meta:
        db_table = 'tbl_publisher'

    def __unicode__(self):
        return '%s %s' % (self.publisher_name, self.address)
