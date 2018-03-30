from django.shortcuts import render
from register.models import Company

# Create your views here.
def index(request):
    companies = Company.objects.all()
    context = {
        'companies' : companies
    }
    return render(request, 'core/index.html', context)

def model(request):
    return render(request, 'core/model.html')
