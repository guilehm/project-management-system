from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('new-user/', views.register, name='new-user'),
    path('new-company/', views.newCompany, name='new-company'),
    path('users/', views.usersView, name='users'),
    path('users/invite/<int:profile_id>/', views.invite, name='invite'),
    path('users/invites/', views.invites, name='invites'),
    path('users/invites/delete/<int:invite_id>/', views.deleteInvite, name='delete-invite'),
]
