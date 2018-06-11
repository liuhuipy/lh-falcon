# -*- coding:utf-8 -*-

from rest_framework import serializers

from common.models import Host, HostGroup, Items, Trigger, Template, Event


class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('id', 'hostname', 'ipaddress', 'macaddress', 'os_type', 'os_version')


class HostGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HostGroup
        fields = ('name', 'description')


class ItemsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = ('name')


class TriggerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trigger
        fields = ('item', 'expression', 'value', 'time')


class TemplateSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Template
        fields = ('name', 'creator', 'trigger')


class EventSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('trigger', 'host', 'item')


