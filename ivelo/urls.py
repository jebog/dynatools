from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="ivelo.index"),
    path("batches/", views.batches, name="ivelo.batches"),
    path("jobs/", views.jobs, name="ivelo.jobs"),
    path("new-batch/", views.create_batch, name="ivelo.new_batch"),
    path("report/", views.report, name="ivelo.report"),
    path("waves/", views.report, name="ivelo.waves"),
]
