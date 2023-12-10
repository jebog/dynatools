from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, "ivelo/index.html")


@login_required
def batches(request):
    return render(request, "ivelo/jobs.html")


@login_required
def create_batch(request):
    return render(request, "ivelo/create-batch.html")


@login_required
def jobs(request):
    return render(request, "ivelo/jobs.html")


@login_required
def report(request):
    return render(request, "ivelo/jobs.html")


@login_required
def waves(request):
    return render(request, "ivelo/waves.html")
