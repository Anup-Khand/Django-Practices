from django.contrib import admin
from .models import student


# Register your models here.
class student_admin(admin.ModelAdmin):
    list_display = ['name', 'address', 'email']


admin.site.register(student, student_admin)
