from django.shortcuts import render, redirect
from .models import Job, Application
from django.contrib.auth.decorators import login_required
@login_required
def home(request):

    return render(request, 'jobs/home.html')

@login_required
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


@login_required
def add_job(request):
    if request.method == 'POST':
        Job.objects.create(
            title=request.POST['title'],
            company=request.POST['company'],
            description=request.POST['description'],
            location=request.POST['location'],
            salary=request.POST['salary'],
            posted_by=request.user
        )
        return redirect('job_list')

    return render(request, 'jobs/add_job.html')


# @login_required
# def apply_job(request, job_id):
#     job = Job.objects.get(id=job_id)

#     if request.method == 'POST':
#         Application.objects.create(
#             user=request.user,
#             job=job,
#             resume=request.FILES['resume']
#         )

#         return redirect('job_list')

#     return render(request, 'jobs/apply.html', {'job': job})

@login_required
def apply_job(request, job_id):

    job = Job.objects.get(id=job_id)

    already_applied = Application.objects.filter(
        user=request.user,
        job=job
    ).exists()

    if already_applied:
        return render(request,
                      'jobs/already_applied.html')

    if request.method == 'POST':

        Application.objects.create(
            user=request.user,
            job=job,
            resume=request.FILES['resume']
        )

        return render(request,
                      'jobs/success.html')

    return render(request,
                  'jobs/apply.html',
                  {'job': job})
    
@login_required
def my_applications(request):

    applications = Application.objects.filter(
        user=request.user
    )

    return render(
        request,
        'jobs/my_applications.html',
        {
            'applications': applications
        }
    )
    
@login_required
def delete_application(request, app_id):

    application = Application.objects.get(
        id=app_id,
        user=request.user
    )

    application.delete()

    return redirect('my_applications')
