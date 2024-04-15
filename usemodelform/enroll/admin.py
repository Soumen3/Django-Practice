from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class adminClass(admin.ModelAdmin):
    list_display=('id', 'name','email','password')