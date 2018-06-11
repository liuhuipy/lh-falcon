# -*- coding:utf-8 -*-

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from common.models import Trigger
from alarm.forms import TriggerForm
from common.mixins import BaseMixin


class TriggerListView(BaseMixin, ListView):
    model = Trigger
    template_name = 'alarm/trigger_list.html'
    context_object_name = 'trigger_list'
    paginate_by = 10

    def get_queryset(self):
        trigger_list = Trigger.objects.order_by('-create_time')
        return trigger_list

    def get_context_data(self, **kwargs):
        kwargs['paginate_by'] = self.paginate_by
        return super(TriggerListView, self).get_context_data(**kwargs)


class TriggerAddView(BaseMixin, CreateView):
    template_name = 'alarm/trigger_add.html'
    form_class = TriggerForm
    success_url = reverse_lazy('alarm:trigger_list')
    success_message = '触发器添加成功！'


class TriggerUpdateView(BaseMixin, UpdateView):
    model = Trigger
    template_name = 'alarm/trigger_edit.html'
    form_class = TriggerForm
    pk_url_kwarg = 'trigger_id'
    success_url = reverse_lazy('alarm:trigger_list')
    success_message = '修改触发器信息成功！'


class TriggerDelView(BaseMixin, DeleteView):
    model = Trigger
    pk_url_kwarg = 'trigger_id'
    success_url = reverse_lazy('alarm:trigger_list')
