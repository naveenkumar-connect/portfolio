from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models



class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'name', 'email',)

admin.site.register(models.UserProfile, UserProfileAdmin) 




