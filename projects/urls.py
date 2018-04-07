from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('new-project/', views.newProject, name='new-project'),
    path('new-task/', views.newTask, name='new-task'),
]