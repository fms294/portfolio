from django.shortcuts import render
from .models import Project


# Create your views here.


def index(request):
    projects = Project.objects.all()
    context ={
        'projects': projects
    }
    return render(request, 'project_index.html', context=context)


def detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context=context)

