from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    user_ip = models.GenericIPAddressField(verbose_name='用户ip', blank=True, null=True)

    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username