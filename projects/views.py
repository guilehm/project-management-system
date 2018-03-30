from django.shortcuts import render
from django.db.models import Avg
from register.models import Project
from projects.models import Task

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    context = {
        'avg_projects' : avg_projects,
        'projects' : projects,
        'tasks' : tasks,
    }
    return render(request, 'projects/projects.html', context)