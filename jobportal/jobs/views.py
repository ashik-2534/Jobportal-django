from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import ApplicationForm

# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    return render (request, 'jobs/job_list.html', {
        'jobs':jobs
    })

def job_details(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/job_detail.html',{
        'job': job
    })

def apply_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('job_details', job_id=job.id)
    else:
        form = ApplicationForm()
    return render (request,'jobs/job_apply.html',{
        'form':form, 'job':job
    })