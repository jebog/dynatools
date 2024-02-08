from django.db import models


class Wave(models.Model):
    name = models.CharField(max_length=100)
    open_date = models.DateTimeField
    launch_date = models.DateTimeField
    status = models.CharField(max_length=30)
    region = models.CharField(max_length=10)

    class Meta(object):
        db_table = 'waves'
        app_label = 'ivelo'
