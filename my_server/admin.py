from django.contrib import admin
from .models import Server
# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'game', 'area', 'version')
    filter_horizontal = ('users',)


admin.site.register(Server, ServerAdmin)
