from django.contrib import admin
from .models import Church
# Register your models here.
@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    list_display = ('name','location')