from django.shortcuts import render
from .models import Project

def index(request):
    return render(request, 'projects/index.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})