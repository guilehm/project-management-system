from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def model(request):
    return render(request, 'core/model.html')