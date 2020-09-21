from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['No','Name','Marks','Address']
    
admin.site.register(Student,StudentAdmin)