from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'full_name', 'assigned_church')}),
    )
    list_display = ('username', 'full_name', 'email', 'role', 'assigned_church')

