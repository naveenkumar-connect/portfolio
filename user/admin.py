"""
registers custom user profiles model to django admin 
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'name', 'email',)

#registering custom user profile to admin
admin.site.register(models.UserProfile, UserProfileAdmin) 




