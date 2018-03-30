from django.shortcuts import render
from django.contrib.auth.models import User
from register.models import Company
from register.models import Project

# Create your views here.
def index(request):
    users = User.objects.all()
    active_users = User.objects.all().filter(is_active=True)
    companies = Company.objects.all()
    projects = Project.objects.all()
    context = {
        'users' : users,
        'active_users' : active_users,
        'companies' : companies,
        'projects' : projects,
    }
    return render(request, 'core/index.html', context)

def model(request):
    return render(request, 'core/model.html')
