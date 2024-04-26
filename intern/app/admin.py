from django.contrib import admin

# Register your models here.
from .models import FirstModel


@admin.register(FirstModel)
class FirstAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email', 'password']
