# -*- coding:utf-8 -*-

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from common.models import TriggerCondition
from alarm.forms import TriggerConditionForm
from common.mixins import BaseMixin


class TriggerConditionListView(BaseMixin, ListView):
    model = TriggerCondition
    template_name = 'alarm/trigger_condition_list.html'
    context_object_name = 'trigger_condition_list'
    paginate_by = 10

    def get_queryset(self):
        trigger_condition_list = TriggerCondition.objects.order_by('-create_time')
        return trigger_condition_list

    def get_context_data(self, **kwargs):
        kwargs['paginate_by'] = self.paginate_by
        return super(TriggerConditionListView, self).get_context_data(**kwargs)


class TriggerCondtionAddView(BaseMixin, CreateView):
    template_name = 'alarm/trigger_condition_add.html'
    form_class = TriggerConditionForm
    success_url = reverse_lazy('alarm:trigger_condition_list')
    success_message = '触发条件添加成功！'


class TriggerConditionUpdateView(BaseMixin, UpdateView):
    model = TriggerCondition
    template_name = 'alarm/trigger_condition_edit.html'
    form_class = TriggerConditionForm
    pk_url_kwarg = 'trigger_condition_id'
    success_url = reverse_lazy('alarm:trigger_condition_list')
    success_message = '修改触发条件信息成功！'


class TriggerConditionDelView(BaseMixin, DeleteView):
    model = TriggerCondition
    pk_url_kwarg = 'trigger_condition_id'
    success_url = reverse_lazy('alarm:trigger_condition_list')
