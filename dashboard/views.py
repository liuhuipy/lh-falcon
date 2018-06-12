from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from users.models import User
from common.models import Host
from common.mixins import BaseMixin


class IndexView(BaseMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        kwargs['host_normal_count'] = Host.objects.filter(is_normal=True).count()
        kwargs['host_measure_count'] = Host.objects.filter(is_normal=False).count()
        kwargs['user_is_staff_count'] = User.objects.filter(is_active=True).count()
        kwargs['user_is_not_staff_count'] = User.objects.filter(is_staff=False).count()
        return super(IndexView, self).get_context_data(**kwargs)


class ItemSearchPictureView(BaseMixin, TemplateView):
    template_name = 'item.html'

    def get_context_data(self, *args, **kwargs):
        kwargs['name'] = 'ansible.node2.com  流量指标'
        kwargs['item_picture_url'] = 'Flow.png'
        return super(ItemSearchPictureView, self).get_context_data(**kwargs)


