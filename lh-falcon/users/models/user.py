# -*- coding:utf-8 -*-
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class Power(models.Model):
    url = models.CharField(max_length=64, unique=True, verbose_name='权限路径')
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')


class UserGroup(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='用户组名')
    power = models.ManyToManyField(Power, null=True, blank=True, verbose_name='拥有权限')
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True, verbose_name='用户名')
    email = models.EmailField(max_length=64, unique=True, verbose_name='邮箱')
    password = models.CharField(max_length=128, verbose_name='密码')
    phone = models.CharField(max_length=11, verbose_name='电话')
    profile = models.CharField(max_length=200, null=True, blank=True, verbose_name='个人简介')
    image = models.ImageField(max_length=200, upload_to='user_images/%Y/%m/%d', default='default.png', verbose_name='用户头像')
    usergroup = models.ForeignKey(UserGroup, verbose_name='角色')
    is_superuser = models.BooleanField(default=False, verbose_name='是否为超级管理员')
    is_active = models.BooleanField(default=False, verbose_name='是否激活')
    is_online = models.BooleanField(default=False, verbose_name='是否在线')
    after_login_url = models.CharField(max_length=100, verbose_name='登陆后url')
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')

    def __str__(self):
        return self.username

