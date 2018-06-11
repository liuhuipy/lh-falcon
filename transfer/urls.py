# -*- coding:utf-8 -*-

from django.conf.urls import url

from transfer.views import HostInfoView, ItemDataReportView


urlpatterns = [
    url(r'api/host/report/$', HostInfoView.as_view(), name='host_report'),
    url(r'api/items/report/$', ItemDataReportView.as_view(), name='item_report'),
]