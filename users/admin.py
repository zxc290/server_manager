from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


class MyUserAdmin(UserAdmin):
    pass


admin.site.register(User, MyUserAdmin)