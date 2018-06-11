# -*- coding:utf-8 -*-

import os
import time

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from django.conf import settings
import rrdtool

from common.models import Host, Template, Items
from common.forms import HostAddForm, HostForm
from common.mixins import BaseMixin


class HostListView(BaseMixin, ListView):
    model = Host
    template_name = 'host/host_list.html'
    context_object_name = 'host_list'
    paginate_by = 10

    def get_queryset(self):
        host_list = Host.objects.order_by('-create_time')

        return host_list

    def get_context_data(self, **kwargs):
        kwargs['paginate_by'] = self.paginate_by
        return super(HostListView, self).get_context_data(**kwargs)


class HostAddView(BaseMixin, CreateView):
    template_name = 'host/host_add.html'
    form_class = HostAddForm
    success_url = reverse_lazy('common:host_list')
    success_messages = '添加主机成功！'


class HostUpdateView(BaseMixin, UpdateView):
    model = Host
    template_name = 'host/host_edit.html'
    form_class = HostForm
    pk_url_kwarg = 'host_id'
    success_url = reverse_lazy('common:host_list')
    success_message = '修改主机信息成功！'


class HostDelView(BaseMixin, DeleteView):
    model = Host
    pk_url_kwarg = 'host_id'
    success_url = reverse_lazy('common:host_list')


class SearchHostView(HostListView):

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q:
            host_list = Host.objects.filter(Q(hostname__contains=q)
                                              | Q(ipaddress__contains=q)
                                              | Q(macaddress__contains=q)
                                              | Q(os_type__contains=q)).order_by('-create_time')
        else:
            host_list = Host.objects.order_by('-create_time')
        return host_list


class HostItemView(BaseMixin, DetailView):
    model = Host
    template_name = 'host/host_item.html'
    pk_url_kwarg = 'host_id'
    redirect_field_name = 'next'

    def get_context_data(self, *args, **kwargs):
        host_id = self.kwargs.get(self.pk_url_kwarg)

        hostgroup = Host.objects.get(id=host_id).hostgroups
        template = Template.objects.get(hostgroup=hostgroup)
        item_list = Items.objects.filter(template=template)
        kwargs['host'] = Host.objects.get(id=host_id)
        kwargs['item_list'] = item_list
        return super(HostItemView, self).get_context_data(**kwargs)


class HostItemGraphView(BaseMixin, DetailView):
    model = Host
    template_name = 'host/host_item.html'
    pk_url_kwarg = 'host_id'
    redirect_field_name = 'next'

    def get_context_data(self, *args, **kwargs):
        base_dir = os.path.join(settings.BASE_DIR, "rrddatas")
        static_dir = os.path.join(settings.STATIC_URL, 'images')
        host_id = self.kwargs.get(self.pk_url_kwarg)
        print(base_dir, static_dir, host_id)
        if self.request.method == 'POST':
            hostname = Host.objects.get(id=host_id).hostname
            item = self.request.POST.get('item')
            rrdname = item + '.rrd'
            name = base_dir +  hostname + '/' + rrdname
            title = item + ' (' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"

            graph_png = static_dir + hostname + '/' + rrdname + '.png'

            hostgroup = Host.objects.get(hostname=hostname).hostgroups
            template = Template.objects.get(hostgroup=hostgroup)
            item_list = Items.objects.filter(template=template)

            # rrdtool.graph(graph_png, '--start', '-1h', '--vertical-label=Bytes/s',
            #               '--x-grid', 'MINUTE:12:HOUR:1:HOUR:1:0:%H',
            #               '--width', '750', '--height', '300', '--title', title,
            #               'DEF:metric=%s:metric:AVERAGE' % (name),
            #               # 'DEF:outoctets=%s:eth0_out:AVERAGE' % (name),
            #               'AREA:metric#00FF00:load 1min',
            #               # 'LINE1:outoctets#0000FF:Out traffic',
            #               'HRULE:190#FF0000:Load value\\r',
            #               'CDEF:data=metric,8,*',
            #               # 'CDEF:outbits=outoctets,8,*',
            #               'COMMENT:\\r',
            #               )
            kwargs['host'] = Host.objects.get(hostname=hostname)
            kwargs['item_list'] = item_list
            kwargs['graph_img'] = graph_png
        return super(HostItemGraphView, self).get_context_data(*args, **kwargs)