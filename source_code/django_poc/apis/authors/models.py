from django.db import models

class Authors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email  = models.CharField(max_length=100)
    class Meta:
        db_table = 'tbl_authors'

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)