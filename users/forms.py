# -*- coding:utf-8 -*-

from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets
from django import forms

from users.models import User, UserGroup


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '50', 'placeholder': '请输入邮箱账号'}),
            'password': widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email', 'password', 'phone', 'user_group', 'is_active', 'is_staff')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'username'}),
            'email': forms.EmailInput(attrs={'class': ' form-control', 'placeholder':'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'password'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'user_group': forms.Select(attrs={'class': 'form-control select2', 'multiple': 'multiple', 'data-placeholder': 'user group'}),
            'is_active': forms.Select(choices=((True, '是'),(False, '否')), attrs={'class': 'form-control','placeholder': 'is_active'}),
            'is_staff': forms.Select(choices=((True, '是'),(False, '否')), attrs={'class': 'form-control select2', 'placeholder': 'is_staff'})
        }
        labels = {
            'username': '用户名',
            'email': '邮箱',
            'password': '密码',
            'phone': '电话',
            'user_group': '用户组',
            'is_active': '是否激活',
            'is_staff': '是否为管理员',
        }
        error_messages = {
            'username': {
                'required': u'请输入用户名',
                'max_length': u'用户名过长',
            },
            'email': {
                'required': u'请输入邮箱',
                'max_length': u'邮箱地址过长',
            },
            'password': {
                'required': u'请输入密码',
                'max_length': u'密码过长',
                'invalid': u'请输入有效邮箱'
            }
        }

    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError(u'用户名必须大于4位')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError(u'密码必须大于6位')
        return password


class UserGroupForm(forms.ModelForm):
    class Meta:
        model = UserGroup
        fields = ('name', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'name'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder':'description'}),
        }
        labels = {
            'name': '用户组名',
            'description': '描述',
        }