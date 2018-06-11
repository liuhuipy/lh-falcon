# -*- coding:utf-8 -*-

from django import forms
from django.forms.widgets import *

from common.models import TriggerCondition, Trigger, AlarmEvent


class TriggerForm(forms.ModelForm):
    class Meta:
        model = Trigger
        fields = ['item','host','expression','value','time']
        widgets = {
            'item': Select(attrs={'class': 'form-control select','placeholder': 'item'}),
            'host': Select(attrs={'class': 'form-control select','placeholder': 'host'}),
            'expression': Select(attrs={'class': 'form-control select','placeholder': 'expression'}),
            'value': TextInput(attrs={'class': 'form-control', 'placeholder': 'value'}),
            'time': TextInput(attrs={'class': 'form-control', 'placeholder': 'time'}),
        }
        labels = {
            'item': '指标',
            'host': '主机',
            'expression': '语法',
            'value': '阀值',
            'time': '次数',
        }


class TriggerConditionForm(forms.ModelForm):
    class Meta:
        model = TriggerCondition
        fields = ['trigger', 'max_time', 'sendee']
        widgets = {
            'trigger': Select(attrs={'class': 'form-control select','placeholder': 'trigger'}),
            'max_time': TextInput(attrs={'class': 'form-control','placeholder': 'max_time'}),
            'sendee': Select(attrs={'class': 'form-control select','placeholder': 'sendee'}),
        }
        labels = {
            'trigger': '触发器',
            'max_time': '最多次数',
            'sendee': '告警接收人',
        }


