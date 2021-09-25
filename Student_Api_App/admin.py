from django.contrib import admin
from Student_Api_App.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 's_name', 's_class', 's_city', 's_lover']


admin.site.register(Student, StudentAdmin)
