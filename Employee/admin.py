from django.contrib import admin
from .models import *

# Register your models here.

class Admin_Department(admin.ModelAdmin):
    list_display = ['dep_name']

class Admin_Emp(admin.ModelAdmin):
    list_display = ['emp_name', 'dep']

class Admin_mypic(admin.ModelAdmin):
    list_display = ['staff']

admin.site.register(Department, Admin_Department)
admin.site.register(Employee, Admin_Emp) 
admin.site.register(mypic, Admin_mypic)