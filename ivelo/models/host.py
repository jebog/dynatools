from django.db import models


class Host(models.Model):
    pass

    class Meta(object):
        db_table = 'hosts'
        app_label = 'ivelo'
