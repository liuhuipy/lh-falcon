# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserGroup(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='用户组名')
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='描述')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '用户组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(max_length=255,unique=True, blank=True, null=True, verbose_name='邮箱')
    username = models.CharField(max_length=32,unique=True, verbose_name='用户名')
    password = models.CharField(max_length=128,verbose_name='密码')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='电话')
    image = models.ImageField(max_length=128, upload_to='user_images/%Y/%m/%d', blank=True, null=True,
                              default='default.png', verbose_name='头像')
    user_group = models.ManyToManyField(UserGroup, related_name='user_group', verbose_name='用户组')
    is_superuser = models.BooleanField(default=False, verbose_name='是否为超级管理员')
    is_staff = models.BooleanField(default=False, verbose_name='是否为管理员')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    is_online = models.BooleanField(default=False, verbose_name='是否在线')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username