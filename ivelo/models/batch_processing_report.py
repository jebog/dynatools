from django.db import models


class BatchProcessingReport(models.Model):
    pass

    class Meta(object):
        db_table = 'batch_processing_report'
        app_label = 'ivelo'
