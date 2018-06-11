# -*- coding:utf-8 -*-

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.shortcuts import HttpResponseRedirect, redirect

from common.models import Template, Items
from common.forms import TemplateForm
from common.mixins import BaseMixin
from users.models import User


class TemplateListView(BaseMixin, ListView):
    model = Template
    template_name = 'host/template_list.html'
    context_object_name = 'template_list'
    paginate_by = 10

    def get_queryset(self):
        template_list = Template.objects.order_by('-create_time')
        return template_list

    def get_context_data(self, **kwargs):
        kwargs['paginate_by'] = self.paginate_by
        return super(TemplateListView, self).get_context_data(**kwargs)


class TemplateAddView(BaseMixin, FormView):
    form_class = TemplateForm
    template_name = 'host/template_add.html'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        return super(TemplateAddView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        name = self.request.POST.get('name')
        username = self.request.user
        items = self.request.POST.getlist('item')
        user = User.objects.get(username=username)

        template = Template.objects.create(name=name, creator=user)
        for item in items:
            template.item.add(Items.objects.get(id=int(item)))
        return redirect('common:template_list')


class TemplateUpdateView(BaseMixin, UpdateView):
    model = Template
    template_name = 'host/template_edit.html'
    form_class = TemplateForm
    pk_url_kwarg = 'template_id'
    success_url = reverse_lazy('common:template_list')
    success_message = '修改模版信息成功！'

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            items = self.request.POST.getlist('item')
            id = self.kwargs.get(self.pk_url_kwarg)
            template = Template.objects.get(id=id)
            for item in items:
                template.item.add(Items.objects.get(id=int(item)))
            return redirect('common:template_list')


class TemplateDelView(BaseMixin, DeleteView):
    model = Template
    pk_url_kwarg = 'template_id'
    success_url = reverse_lazy('common:template_list')
