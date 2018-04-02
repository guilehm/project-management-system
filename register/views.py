from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from projects.models import Task
from .models import UserProfile
from .models import Invite
from .forms import RegistrationForm
from .forms import CompanyRegistrationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            user = form.save()
            created = True
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context = {'created' : created}
            return render(request, 'register/reg_form.html', context)
        else:
            return render(request, 'register/reg_form.html', context)
    else:
        form = RegistrationForm()
        context = {
            'form' : form,
        }
        return render(request, 'register/reg_form.html', context)




def usersView(request):
    users = User.objects.all()
    tasks = Task.objects.all()
    context = {
        'users': users,
        'tasks': tasks,
    }
    return render(request, 'register/users.html', context)


def newCompany(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
            created = True
            form = CompanyRegistrationForm()
            context = {
                'created' : created,
                'form' : form,
                       }
            return render(request, 'register/new_company.html', context)
        else:
            return render(request, 'register/new_company.html', context)
    else:
        form = CompanyRegistrationForm()
        context = {
            'form' : form,
        }
        return render(request, 'register/new_company.html', context)


def invites(request):
    return render(request, 'register/invites.html')


def invite(request, profile_id):
    profile_to_invite = UserProfile.objects.get(id=profile_id)
    logged_profile = get_active_profile(request)
    logged_profile.invite(profile_to_invite)
    return redirect('core:index')


def deleteInvite(request, invite_id):
    logged_user = get_active_profile(request)
    logged_user.received_invites.get(id=invite_id).delete()
    return render(request, 'register/invites.html')


def acceptInvite(request, invite_id):
    invite = Invite.objects.get(id=invite_id)
    invite.accept()
    return redirect('register:invites')


def get_active_profile(request):
    user_id = request.user.userprofile_set.values_list()[0][0]
    return UserProfile.objects.get(id=user_id)

