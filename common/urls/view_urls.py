# -*- coding:utf-8 -*-

from django.conf.urls import url
from common.views import host, hostgroup, items, template


urlpatterns = [
    # host action url
    url(r'host/list/$', host.HostListView.as_view(), name='host_list'),
    url(r'host/add/$', host.HostAddView.as_view(), name='host_add'),
    url(r'host/edit/(?P<host_id>\d+)/$', host.HostUpdateView.as_view(), name='host_edit'),
    url(r'host/del/(?P<host_id>\d+)/$', host.HostDelView.as_view(), name='host_del'),
    url(r'host/search/$', host.SearchHostView.as_view(), name='host_search'),
    url(r'host/item_list/(?P<host_id>\d+)/$', host.HostItemView.as_view(), name='host_item'),
    url(r'host/item_graph/(?P<host_id>\d+)/$', host.HostItemView.as_view(), name='host_item_graph'),

    # hostgroup action url
    url(r'hostgroup/list/$', hostgroup.HostGroupListView.as_view(), name='hostgroup_list'),
    url(r'hostgroup/add/$', hostgroup.HostGroupAddView.as_view(), name='hostgroup_add'),
    url(r'hostgroup/edit/(?P<hostgroup_id>\d+)/$', hostgroup.HostGroupUpdateView.as_view(), name='hostgroup_edit'),
    url(r'hostgroup/del/(?P<hostgroup_id>\d+)/$', hostgroup.HostGroupDelView.as_view(), name='hostgroup_del'),

    # item action url
    url(r'item/list/$', items.ItemsListView.as_view(), name='item_list'),
    url(r'item/add/$', items.ItemsAddView.as_view(), name='item_add'),
    url(r'item/del/(?P<item_id>\d+)/$', items.ItemsDelView.as_view(), name='item_del'),

    # template action url
    url(r'template/list/$', template.TemplateListView.as_view(), name='template_list'),
    url(r'template/add/$', template.TemplateAddView.as_view(), name='template_add'),
    url(r'template/edit/(?P<template_id>\d+)/$', template.TemplateUpdateView.as_view(), name='template_edit'),
    url(r'template/del/(?P<template_id>\d+)/$', template.TemplateDelView.as_view(), name='template_del'),
]