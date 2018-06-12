from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    filter_horizontal = ('servers',)


admin.site.register(User, MyUserAdmin)