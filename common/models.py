from django.db import models

from users.models import User


class Items(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='指标名')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '指标'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='模版名')
    creator = models.ForeignKey(User, verbose_name='创建者')
    item = models.ManyToManyField(Items, verbose_name='指标')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '模版'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class HostGroup(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='主机组名')
    template = models.ForeignKey('Template', blank=True, verbose_name='绑定模版')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '主机组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Host(models.Model):
    hostname = models.CharField(max_length=32, unique=True, verbose_name='主机名')
    ipaddress = models.GenericIPAddressField(unique=True, blank=True, null=True, verbose_name='IP地址')
    macaddress = models.CharField(max_length=32, unique=True, blank=True, null=True, verbose_name='MAC地址')
    os_type = models.CharField(max_length=32, blank=True, null=True, verbose_name='操作系统类型')
    os_version = models.CharField(max_length=64, blank=True, null=True, verbose_name='操作系统版本')
    hostgroups = models.ForeignKey(HostGroup, blank=True, verbose_name='主机组')

    is_normal = models.BooleanField(default=True, verbose_name='是否正常')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '主机组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hostname


class Trigger(models.Model):
    EXPRESSION_TYPE_CHOICES = (
        ('>', '>'),
        ('=', '='),
        ('<', '<'),
        ('!=', '!='),
    )
    item = models.ForeignKey(Items, verbose_name='指标')
    host = models.ForeignKey(Host, verbose_name='主机')
    expression = models.CharField(max_length=16, choices=EXPRESSION_TYPE_CHOICES, default='>', blank=True, verbose_name='语法')
    value = models.CharField(max_length=16, verbose_name='阈值')
    time = models.SmallIntegerField(default=0, verbose_name='触发次数')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '触发器'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.host.hostname + ':' +  self.item.name + ' is ' + self.expression + self.value


class TriggerCondition(models.Model):
    trigger = models.ForeignKey(Trigger, verbose_name='Trigger')
    max_time = models.SmallIntegerField(default=3, verbose_name='触发报警事件的次数')

    sendee = models.ManyToManyField(User, verbose_name='告警接收人')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '告警触发条件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class AlarmEvent(models.Model):
    ALARM_TYPE_CHOICES = (
        ('list', 'List'),
        ('sms', 'Sms'),
        ('email', 'Email'),
    )

    host = models.ForeignKey(Host, verbose_name='告警主机')
    item = models.ForeignKey(Items, verbose_name='告警指标')
    time = models.SmallIntegerField(default=3, verbose_name='阈值触发的次数')

    alarm_type = models.CharField(max_length=32, choices=ALARM_TYPE_CHOICES, default='list', verbose_name='告警方式')
    is_solut = models.BooleanField(default=False, verbose_name='是否解决')

    start_time = models.DateTimeField(auto_now_add=True, verbose_name='告警开始时间')
    end_time = models.DateTimeField(auto_now=True, verbose_name='告警解决时间')

    class Meta:
        verbose_name = '告警事件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id