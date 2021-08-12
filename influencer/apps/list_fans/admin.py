from django.contrib import admin
from .models import Interest, FanInterest, AgeRange, FanAgeRange

# Register your models here.

@admin.register(Interest, FanInterest, AgeRange, FanAgeRange)
class FansListAdmin(admin.ModelAdmin):
    pass