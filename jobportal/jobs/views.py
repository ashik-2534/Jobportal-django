from django.shortcuts import render
from .models import Job

# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    return render (request, 'job/job_list.html', {
        'jobs':jobs
    })