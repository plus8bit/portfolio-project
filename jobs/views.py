from django.shortcuts import render
from .models import Job

def home_view(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})

