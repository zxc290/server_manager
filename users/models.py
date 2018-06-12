from django.db import models
from django.contrib.auth.models import AbstractUser
from my_server.models import Server


# Create your models here.
class User(AbstractUser):
    user_ip = models.GenericIPAddressField(verbose_name='用户ip', blank=True, null=True)
    servers = models.ManyToManyField(Server, blank=True, related_name='server_owner', verbose_name='用户管理的服务器')

    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username