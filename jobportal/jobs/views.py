from django.shortcuts import render
from .models import Job

# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    return render (request, 'jobs/job_list.html', {
        'jobs':jobs
    })