from django.contrib import admin

# Register your models here.
from user import models
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'password', 'power', 'is_valid', 'created_time')
    list_per_page = 10
    ordering = ['-created_time']
