from django.shortcuts import render
from register.models import Company

# Create your views here.
def projects(request):
    return render(request, 'projects/projects.html')