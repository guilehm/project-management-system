from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','email','city','found_date']
    search_fields = ['name', 'social_name','city']

# Register your models here.
admin.site.register(Company, CompanyAdmin)