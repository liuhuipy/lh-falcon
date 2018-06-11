# -*- coding:utf-8 -*-

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from common.models import AlarmEvent
from common.forms import HostForm
from common.mixins import BaseMixin


class AlarmEventListView(BaseMixin, ListView):
    model = AlarmEvent
    template_name = 'alarm/alarm_event_list.html'
    context_object_name = 'alarm_event_list'
    paginate_by = 10

    def get_queryset(self):
        alarm_event_list = AlarmEvent.objects.order_by('-start_time')
        return alarm_event_list

    def get_context_data(self, **kwargs):
        kwargs['paginate_by'] = self.paginate_by
        return super(AlarmEventListView, self).get_context_data(**kwargs)


class AlarmEventUpdateView(BaseMixin, UpdateView):
    model = AlarmEvent
    template_name = 'alarm/alarm_event_edit.html'
    form_class = HostForm
    pk_url_kwarg = 'alarm_event_id'
    success_url = reverse_lazy('alarm:alarm_event_list')


class AlarmEventDelView(BaseMixin, DeleteView):
    model = AlarmEvent
    pk_url_kwarg = 'alarm_event_id'
    success_url = reverse_lazy('alarm:alarm_event_list')