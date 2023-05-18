from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'gender', 'salary', 'wealth', 'tendency')
    fields = ('username', 'password', 'age', 'gender', 'salary', 'wealth', 'tendency')
    
admin.site.register(User,UserAdmin)