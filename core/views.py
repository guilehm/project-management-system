from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect
from register.models import Company
from register.models import Project
from projects.models import Task
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def dashboard(request):
    users = User.objects.all()
    active_users = User.objects.all().filter(is_active=True)
    companies = Company.objects.all()
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'users' : users,
        'active_users' : active_users,
        'companies' : companies,
        'projects' : projects,
        'tasks' : tasks,
    }
    return render(request, 'core/dashboard.html', context)


def model(request):
    return render(request, 'core/model.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            return redirect('core:index')
        else:
            return render(request, 'register/login.html', {'login_form':form})
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'login_form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:index'))