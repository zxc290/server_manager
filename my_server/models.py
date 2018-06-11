from django.db import models

# Create your models here.
class Server(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='服务器地址', unique=True)
    game = models.CharField(max_length=30, verbose_name='游戏名')
    area = models.CharField(max_length=30, verbose_name='游戏区服')
    version = models.CharField(default='v1.0', max_length=30, verbose_name='游戏版本')
    last_update = models.DateTimeField(auto_now=True, verbose_name='最近编辑时间')

    class meta:
        ordering = ['last_update']
        verbose_name = '服务器信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip_address

