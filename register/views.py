from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
            print('form é válido')
            return redirect('core:index')
        else:
            print('form não é válido')
            return render(request, 'register/reg_form.html', context)
    else:
        form = RegistrationForm()
        context = {
            'form' : form,
        }
        print('situação2')
        return render(request, 'register/reg_form.html', context)