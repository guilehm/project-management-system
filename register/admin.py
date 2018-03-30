from django.contrib import admin
from .models import Company
from .models import UserProfile


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','email','city','found_date']
    search_fields = ['name', 'social_name','city']

# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(UserProfile)