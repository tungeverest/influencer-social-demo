from django.contrib import admin
from .models import (
    UserModel, Employee
)

from django.contrib.auth.models import Permission

# Register your models here.

@admin.register(
    UserModel, Employee, Permission
)
class UserAdmin(admin.ModelAdmin):
    pass