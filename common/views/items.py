# -*- coding:utf-8 -*-

from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy

from common.models import Items
from common.forms import ItemForm
from common.mixins import BaseMixin


class ItemsListView(BaseMixin, ListView):
    model = Items
    template_name = 'host/item_list.html'
    context_object_name = 'item_list'
    paginate_by = 10

    def get_queryset(self):
        item_list = Items.objects.order_by('-create_time')
        return item_list

    def get_context_data(self, **kwargs):
        kwargs['paginate_by'] = self.paginate_by
        return super(ItemsListView, self).get_context_data(**kwargs)


class ItemsAddView(BaseMixin, CreateView):
    template_name = 'host/item_add.html'
    form_class = ItemForm
    success_url = reverse_lazy('common:item_list')
    success_message = '指标添加成功！'


class ItemsDelView(BaseMixin, DeleteView):
    model = Items
    pk_url_kwarg = 'item_id'
    success_url = reverse_lazy('common:item_list')
