# -*- coding:utf-8 -*-
from django.db import models


class Items(models.Model):
    """
    监控项：
    被监控服务器通过agent、SNMP或其他方式采集的数十上百个甚至更多监控项
    """
    ITEM_TYPE = (
        (1, 'lh-falcon agent'),
        (2, 'SNMP agent'),
        (3, 'SSH agent'),
        (4, 'IPMI agent'),
        (5, 'Database monitor'),
    )
    STORE_VALUE = (
        ('As is', 'As is'),
        ('Delta speed', 'Delta speed'),
    )
    name = models.CharField(max_length=100, unique=True, verbose_name='监控项名称')
    item_type = models.IntegerField(choices=ITEM_TYPE, verbose_name='监控类型')
    key = models.CharField(max_length=100, unique=True, verbose_name='监控项')
    parameter = models.CharField(max_length=100, null=True, blank=True, verbose_name='参数')
    update_interval = models.IntegerField(default=30, verbose_name='数据更新时间')
    store_value = models.CharField(max_length=50, choices=STORE_VALUE, verbose_name='数据类型')
    application = models.ForeignKey(Applications, null=True, blank=True, verbose_name='应用')
    Description = models.TextField(max_length=200, null=True, blank=True, verbose_name='描述')
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')

    def __str__(self):
        return self.key