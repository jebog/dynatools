from django.db import models


class ApScheduler(models.Model):
    next_run_time = models.DateTimeField()
    job_date = models.DateTimeField()

    class Meta(object):
        db_table = 'ap_scheduler'
        app_label = 'ivelo'
