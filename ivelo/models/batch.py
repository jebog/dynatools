from django.contrib.auth.models import User
from django.db import models

from ivelo.models.wave import Wave


class Batch(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    operation_type = models.CharField(max_length=30)
    inventory_script = models.CharField(max_length=255)
    status = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    report = models.CharField(max_length=100)
    wave_id = models.ForeignKey(Wave, on_delete=models.CASCADE, null=True, blank=True)
    ansible_tower_platform = models.CharField(max_length=100, null=True)

    class Meta(object):
        db_table = 'batches'
        app_label = 'ivelo'
