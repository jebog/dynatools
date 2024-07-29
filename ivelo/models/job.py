from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    ansible_payload = models.TextField()
    ansible_job_id = models.PositiveIntegerField()
    end_date = models.DateTimeField(null=True)
    ansible_tower_platform = models.CharField(max_length=100)

    class Meta(object):
        db_table = 'jobs'
        app_label = 'ivelo'
