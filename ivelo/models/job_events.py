from django.db import models

from ivelo.models.job import Job


class JobEvent(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    host_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    error = models.TextField()
    error_message = models.TextField()
    task = models.CharField(max_length=100)
    playbook = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    stdout = models.TextField()
    network_zone = models.CharField(max_length=30)
    app_id = models.PositiveIntegerField()
    app_name = models.CharField(max_length=100)
    install_mode = models.CharField(max_length=100)
    os_type = models.CharField(max_length=100)
    region = models.CharField(max_length=10, null=True)
    tags_fields = models.TextField()

    class Meta(object):
        db_table = 'job_events'
        app_label = 'ivelo'
