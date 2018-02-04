# -*- coding:utf-8 -*-
import datetime

from django.db import models


class Applications(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='应用')

    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')

