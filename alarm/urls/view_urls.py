# -*- coding:utf-8 -*-

from django.conf.urls import url
from alarm.views import trigger, trigger_condition, alarm_event


urlpatterns = [
    # trigger action url
    url(r'trigger/list/$', trigger.TriggerListView.as_view(), name='trigger_list'),
    url(r'trigger/add/$', trigger.TriggerAddView.as_view(), name='trigger_add'),
    url(r'trigger/edit/(?P<trigger_id>\d+)/$', trigger.TriggerUpdateView.as_view(), name='trigger_edit'),
    url(r'trigger/del/(?P<trigger_id>\d+)/$', trigger.TriggerDelView.as_view(), name='trigger_del'),

    # trigger_condition action url
    url(r'trigger/condition/list/$', trigger_condition.TriggerConditionListView.as_view(), name='trigger_condition_list'),
    url(r'trigger/condition/add/$', trigger_condition.TriggerCondtionAddView.as_view(), name='trigger_condition_add'),
    url(r'trigger/condition/edit/(?P<trigger_condition_id>\d+)/$', trigger_condition.TriggerConditionUpdateView.as_view(), name='trigger_condition_edit'),
    url(r'trigger/condition/del/(?P<trigger_condition_id>\d+)/$', trigger_condition.TriggerConditionDelView.as_view(), name='trigger_condition_del'),

    # alarm_event action url
    url(r'alarmevent/list/$', alarm_event.AlarmEventListView.as_view(), name='alarm_event_list'),
    url(r'alarmevent/edit/(?P<alarm_event_id>\d+)/$', alarm_event.AlarmEventUpdateView.as_view(), name='alarm_event_edit'),
    url(r'alarmevent/del/(?P<alarm_event_id>\d+)/$', alarm_event.AlarmEventDelView.as_view(), name='alarm_event_del'),
]