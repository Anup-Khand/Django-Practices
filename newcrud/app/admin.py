from django.contrib import admin
from .models import UserMod
# Register your models here.


@admin.register(UserMod)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "password"]
