# -*- coding:utf-8 -*-

from django import forms
from django.forms.widgets import *

from common.models import Host, HostGroup, Items, Template


class HostAddForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['hostname', 'hostgroups']
        widgets = {
            'hostname': TextInput(attrs={'class': 'form-control','placeholder': 'hostname'}),
            'hostgroups': Select(attrs={'class': 'form-control','placeholder': 'hostgroup'}),
        }
        labels = {
            'hostname': '主机名',
            'hostgroups': '所属主机组',
        }


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['hostname','ipaddress','macaddress','os_type','os_version']
        widgets = {
            'hostname': TextInput(attrs={'class': 'form-control','placeholder': 'hostname'}),
            'ipaddress': TextInput(attrs={'class': 'form-control', 'data-inputmask': "'alias': 'ip'",
                                         'data-mask': '', 'placeholder': 'ipaddress'}),
            'macaddress': TextInput(attrs={'class': 'form-control', 'placeholder': 'macaddress'}),
            'os_type': TextInput(attrs={'class': 'form-control', 'placeholder': 'os_type'}),
            'os_version': TextInput(attrs={'class': 'form-control', 'placeholder': 'os_version'}),
        }
        labels = {
            'hostname': '主机名',
            'ipaddress': 'IP地址',
            'macaddress': 'MAC地址',
            'os_type': '操作系统类型',
            'os_version': '操作系统版本',
        }


class HostGroupForm(forms.ModelForm):
    class Meta:
        model = HostGroup
        fields = ['name', 'template', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','placeholder': 'hostgroup name'}),
            'template': Select(attrs={'class': 'form-control','placeholder': 'template'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }
        labels = {
            'name': '主机组名',
            'template': '模版',
            'description': '描述',
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'form-control','placeholder': 'item name'})}


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'item']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control','placeholder': 'name'}),
            'item': Select(attrs={'class': 'form-control select2', 'id': 'items', 'multiple': 'multiple', 'placeholder': 'hostgroup name'}),
        }

