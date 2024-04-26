from django.contrib import admin
from .models import Student, School


class Student_admin(admin.ModelAdmin):
    list_display = ['name', 'roll_no', 'address']


admin.site.register(Student, Student_admin)


class School_admin(admin.ModelAdmin):
    list_display = ['name', 'address','Role']


admin.site.register(School, School_admin)
