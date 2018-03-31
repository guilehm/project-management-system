from django.contrib import admin
from .models import Project
from .models import Task

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    raw_id_fields = ('company',)
    list_display = ['name', 'company', ]
    list_filter = ['name', 'company', ]
    search_fields = ['name', 'company', 'status',]
    prepopulated_fields = {'slug':('name',)}

    class Meta:
        model = Project

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name','project']
    list_filter = ['project', ]
    search_fields = ['project']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)