from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('new-user/', views.register, name='new-user'),
    path('new-company/', views.newCompany, name='new-company'),
    path('users/', views.usersView, name='users'),
    path('users/invite/(?P<profile_id>\d+)/$', views.invite, name='invite'),
]
