# -*- coding:utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.shortcuts import redirect,HttpResponseRedirect
from django.urls import reverse

from common.models import Host, HostGroup, Trigger, TriggerCondition, AlarmEvent, Items, Template
from users.models import User,UserGroup


class BaseMixin(LoginRequiredMixin):
    login_url = 'users:login'
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin, self).get_context_data(*args, **kwargs)
        context['host_count'] = Host.objects.all().count()
        context['hostgroup_count'] = HostGroup.objects.all().count()
        context['item_count'] = Items.objects.all().count()
        context['template_count'] = Template.objects.all().count()

        context['user_count'] = User.objects.all().count()
        context['usergroup_count'] = UserGroup.objects.all().count()

        context['trigger_count'] = Trigger.objects.all().count()
        context['trigger_condition_count'] = TriggerCondition.objects.all().count()
        context['alarm_event_count'] = AlarmEvent.objects.all().count()

        return context


class ActionPermissionRequiredMixin(PermissionRequiredMixin):
    """
    CBV mixin which verifies that the current user has all specified
    permissions.
    """
    def dispatch(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get(self.pk_url_kwarg)
            if not request.user.is_staff and not request.user.is_superuser \
                    and str(request.user.id) != pk:
                return HttpResponseRedirect(reverse('permission:no_action_permission'))
        except:
            if not request.user.is_staff and not request.user.is_superuser:
                return HttpResponseRedirect(reverse('permission:no_action_permission'))
        return super(PermissionRequiredMixin, self).dispatch(request, *args, **kwargs)
