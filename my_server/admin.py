from django.contrib import admin
from .models import Server
# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'game', 'area', 'version')

admin.site.register(Server, ServerAdmin)