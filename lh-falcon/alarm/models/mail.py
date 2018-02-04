# -*- coding:utf-8 -*-

from django.db import models


class Mail(models.Model):
    mail = models.CharField(max_length=100, verbose_name='邮箱地址')




