from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'tbl_category'

    def __unicode__(self):
        return '%s %s' % (self.cat_name)