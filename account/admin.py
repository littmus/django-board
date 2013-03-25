from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = User
    fk_name = 'user'
    max_num = 1


#class CustomUserAdmin(UserAdmin):
#    inlines = [ProfileInline,]


#admin.site.register(User, CustomUserAdmin)